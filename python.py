def calculate_bmi(weight, height, units):
    if units.lower() == 'metric':
        bmi = weight / (height ** 2)
    elif units.lower() == 'imperial':
        bmi = (weight * 703) / (height ** 2)
    else:
        print("Invalid choice of units. Please select 'metric' or 'imperial'.")
        return None

    return bmi


def get_bmi_classification(bmi, gender):
    if gender.lower() == 'male':
        if bmi < 20.7:
            return 'Underweight'
        elif 20.7 <= bmi < 26.4:
            return 'Normal weight'
        elif 26.4 <= bmi < 27.8:
            return 'Slightly overweight'
        elif 27.8 <= bmi < 31.1:
            return 'Overweight'
        else:
            return 'Obese'
    elif gender.lower() == 'female':
        if bmi < 19.1:
            return 'Underweight'
        elif 19.1 <= bmi < 25.8:
            return 'Normal weight'
        elif 25.8 <= bmi < 27.3:
            return 'Slightly overweight'
        elif 27.3 <= bmi < 32.3:
            return 'Overweight'
        else:
            return 'Obese'
    else:
        print("Invalid gender. Please enter 'male' or 'female'.")
        return None


def main():
    print("Advanced BMI Calculator")
    print("-----------------------")
    gender = input("Enter your gender (male/female): ")
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    units = input("Enter your choice of units (metric/imperial): ")

    bmi = calculate_bmi(weight, height, units)
    if bmi is not None:
        classification = get_bmi_classification(bmi, gender)
        if classification is not None:
            print("\nBMI Classification:")
            print("BMI: {:.2f}".format(bmi))
            print("Classification: {}".format(classification))


if __name__ == '__main__':
    main()
