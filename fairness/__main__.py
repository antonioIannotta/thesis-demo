from fairness.metric import find_metric_by_name

while True:
    class_name = input("Enter the name of the class you want to test: ")
    print(find_metric_by_name(class_name))
