#NUMPY STATISTICS DASHBORAD

import numpy as np

while True:
    print("\n==============================")
    print("   NUMPY STATISTICS DASHBOARD")
    print("==============================")

    print("1. Enter Numbers")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "2":
        print("Thank You!")
        break

    elif choice == "1":

        nums = list(map(float, input("\nEnter numbers separated by space: ").split()))

        arr = np.array(nums)

        while True:

            print("\n----------- Dashboard -----------")
            print("1. Show Array")
            print("2. Mean")
            print("3. Median")
            print("4. Maximum")
            print("5. Minimum")
            print("6. Sum")
            print("7. Standard Deviation")
            print("8. Variance")
            print("9. Sort Array")
            print("10. Search Number")
            print("11. Enter New Data")
            print("12. Exit")

            ch = input("Enter Choice: ")

            if ch == "1":
                print("\nArray =", arr)

            elif ch == "2":
                print("\nMean =", np.mean(arr))

            elif ch == "3":
                print("\nMedian =", np.median(arr))

            elif ch == "4":
                print("\nMaximum =", np.max(arr))

            elif ch == "5":
                print("\nMinimum =", np.min(arr))

            elif ch == "6":
                print("\nSum =", np.sum(arr))

            elif ch == "7":
                print("\nStandard Deviation =", np.std(arr))

            elif ch == "8":
                print("\nVariance =", np.var(arr))

            elif ch == "9":
                print("\nSorted Array =", np.sort(arr))

            elif ch == "10":
                num = float(input("Enter number to search: "))

                if num in arr:
                    index = np.where(arr == num)[0]
                    print("Number Found at Index:", index)
                else:
                    print("Number Not Found")

            elif ch == "11":
                break

            elif ch == "12":
                exit()

            else:
                print("Invalid Choice")

    else:
        print("Invalid Choice")