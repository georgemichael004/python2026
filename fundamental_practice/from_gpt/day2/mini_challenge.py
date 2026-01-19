# Task: Count how many scores passed vs failed based on a threshold.
def pass_fail(input_list):
    passed = 0
    failed = 0
    for marks in input_list:
        if marks >= 60:
            passed += 1
        else:
            failed += 1
    return (f"passed {passed}, failed {failed}")

print(pass_fail([5,67, 34, 34, 78, 90]))
