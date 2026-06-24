from abc import ABC, abstractmethod

# ==================================================
# S - Single Responsibility Principle (SRP)
# A class should have only one reason to change.
# ==================================================

class Report:
    def __init__(self, content):
        self.content = content

class ReportPrinter:
    def print_report(self, report):
        print(f"Printing Report: {report.content}")


# ==================================================
# O - Open/Closed Principle (OCP)
# Open for extension, closed for modification.
# ==================================================

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

def calculate_area(shape: Shape):
    return shape.area()


# ==================================================
# L - Liskov Substitution Principle (LSP)
# Subtypes should be replaceable for base types.
# ==================================================

class Bird:
    def move(self):
        print("Bird is moving")

class FlyingBird(Bird):
    def move(self):
        print("Flying in the sky")

class Sparrow(FlyingBird):
    pass

def bird_action(bird: Bird):
    bird.move()


# ==================================================
# I - Interface Segregation Principle (ISP)
# Clients should not depend on methods they don't use.
# ==================================================

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

class Robot(Workable):
    def work(self):
        print("Robot is working")


# ==================================================
# D - Dependency Inversion Principle (DIP)
# Depend on abstractions, not concrete classes.
# ==================================================

class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(MessageService):
    def send(self, message):
        print(f"Email sent: {message}")

class SMSService(MessageService):
    def send(self, message):
        print(f"SMS sent: {message}")

class Notification:
    def __init__(self, service: MessageService):
        self.service = service

    def notify(self, message):
        self.service.send(message)


# ==================================================
# Main Program
# ==================================================

if __name__ == "__main__":

    print("=== SRP Example ===")
    report = Report("Monthly Sales Report")
    printer = ReportPrinter()
    printer.print_report(report)

    print("\n=== OCP Example ===")
    rect = Rectangle(10, 5)
    circle = Circle(7)

    print("Rectangle Area:", calculate_area(rect))
    print("Circle Area:", calculate_area(circle))

    print("\n=== LSP Example ===")
    sparrow = Sparrow()
    bird_action(sparrow)

    print("\n=== ISP Example ===")
    human = Human()
    robot = Robot()

    human.work()
    human.eat()
    robot.work()

    print("\n=== DIP Example ===")
    email_notification = Notification(EmailService())
    sms_notification = Notification(SMSService())

    email_notification.notify("Welcome!")
    sms_notification.notify("Your OTP is 1234")