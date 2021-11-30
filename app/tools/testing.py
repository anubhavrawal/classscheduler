from  ...senior_design.scheduler.models import Instructors

def main():
    a = Instructors.objects.get(id = 1)
    print(a.first_name)
    return

if __name__ == "__main__":
    main()