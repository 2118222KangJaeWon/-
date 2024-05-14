def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):

    if bmi < 18.5:
        return "저체중"
    elif 18.5 <= bmi < 25:
        return "정상"
    elif 25 <= bmi < 30:
        return "과체중"
    elif 30 <= bmi < 35:
        return "비만 (1단계)"
    elif 35 <= bmi < 40:
        return "비만 (2단계)"
    else:
        return "고도 비만"

def main():

    weight = float(input("몸무게를 kg 단위로 입력하세요: "))
    height = float(input("키를 미터 단위로 입력하세요: "))


    bmi = calculate_bmi(weight, height)


    print("당신의 BMI 지수는 {:.2f} 이고, 비만의 정도는 {}입니다.".format(bmi, interpret_bmi(bmi)))

if __name__ == "__main__":
    main()