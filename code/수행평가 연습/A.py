import csv
from types import SimpleNamespace


class Student:
    def __init__(self, name, fixed_seat, preferred_seat, prev_seat, prev_partner):
        self.name = name
        self.fixed_seat = fixed_seat
        self.preferred_seat = preferred_seat
        self.prev_seat = prev_seat
        self.prev_partner = prev_partner


class Classroom:
    def __init__(self, rows, cols, allow_prev_partner=False, allow_prev_seat=False):
        self.rows = rows
        self.cols = cols
        self.allow_prev_partner = allow_prev_partner
        self.allow_prev_seat = allow_prev_seat
        self.seats = [[None for _ in range(cols)] for _ in range(rows)]

    def get_partner(self, row, col):
        partner_col = col + 1 if col % 2 == 0 else col - 1
        if 0 <= partner_col < self.cols:
            return self.seats[row][partner_col]
        return None

    def display_seats(self):
        for seat_row in self.seats:
            names = []
            for student in seat_row:
                names.append("빈자리" if student is None else student.name)
            print(" ".join(names))


def parse_seat(text):
    if text == "-":
        return None
    row, col = map(int, text.split("_"))
    return row, col


def seat_text(seat):
    return "-" if seat is None else f"{seat[0]}_{seat[1]}"


def load_students_data(file_path):
    students = []
    with open(file_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            preferred_seat = {
                "front": int(row["preferred_front"]) if row["preferred_front"] else 0,
                "back": int(row["preferred_back"]) if row["preferred_back"] else 0,
            }
            student = Student(
                name=row["name"],
                fixed_seat=parse_seat(row["fixed_seat"] or "-"),
                preferred_seat=preferred_seat,
                prev_seat=parse_seat(row["previous_seat"] or "-"),
                prev_partner=row["previous_partner"] or None,
            )
            students.append(student)
    return students


def assign_fixed(classroom, students):
    remaining_students = []
    for student in students:
        if student.fixed_seat is not None:
            row, col = student.fixed_seat
            if not (0 <= row < classroom.rows and 0 <= col < classroom.cols):
                raise ValueError(f"[고정석 오류] ({row}, {col}) 은 교실 범위를 벗어남.")

            if classroom.seats[row][col] is not None:
                raise ValueError(f"[고정석 오류] ({row}, {col})은 이미 배정됨.")

            classroom.seats[row][col] = student
        else:
            remaining_students.append(student)
    return remaining_students


def read_student_record(line):
    name, fixed, front, back, previous, partner = line.rstrip("\n").split("|")
    preferred = {
        "front": int(front),
        "back": int(back),
    }
    return Student(
        name,
        parse_seat(fixed),
        preferred,
        parse_seat(previous),
        None if partner == "-" else partner,
    )


def print_student(student):
    print("|".join([
        student.name,
        seat_text(student.fixed_seat),
        str(student.preferred_seat["front"]),
        str(student.preferred_seat["back"]),
        seat_text(student.prev_seat),
        student.prev_partner if student.prev_partner is not None else "-",
    ]))


def main():
    mode = input().strip()
    if mode == "STUDENT":
        count = int(input())
        for _ in range(count):
            print_student(read_student_record(input()))
        return

    if mode == "DISPLAY":
        rows, cols = map(int, input().split())
        classroom = Classroom(rows, cols)
        for row in range(rows):
            values = input().split()
            for col, name in enumerate(values):
                if name != "-":
                    classroom.seats[row][col] = SimpleNamespace(name=name)
        classroom.display_seats()
        return

    if mode == "ASSIGN":
        rows, cols = map(int, input().split())
        students = []
        for _ in range(int(input())):
            name, fixed = input().strip().split("|")
            students.append(SimpleNamespace(name=name, fixed_seat=parse_seat(fixed)))
    elif mode == "CSV":
        classroom = Classroom(4, 4)
        students = load_students_data("students.csv")
    else:
        raise ValueError("지원하지 않는 실행 모드입니다.")

    if mode == "ASSIGN":
        classroom = Classroom(rows, cols)

    try:
        remaining = assign_fixed(classroom, students)
    except ValueError as error:
        print(f"ERROR: {error}")
        return

    classroom.display_seats()
    names = ",".join(student.name for student in remaining)
    print(f"남은 학생: {names if names else '없음'}")


if __name__ == "__main__":
    main()