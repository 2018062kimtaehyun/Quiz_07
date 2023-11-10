import random

def generate_lotto_numbers():
    lotto_numbers = []

    while len(lotto_numbers) < 6:
        number = random.randint(1, 45)

        if number not in lotto_numbers:
            lotto_numbers.append(number)

    lotto_numbers.sort()
    return lotto_numbers

def main():
    generated_numbers = generate_lotto_numbers()
    numbers_str = ', '.join(map(str, generated_numbers))
    print(f"생성된 로또 번호는 {numbers_str} 입니다")

if __name__ == "__main__":
    main()
