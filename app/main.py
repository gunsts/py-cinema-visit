from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.customer import Customer
from people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = [Customer(customer["name"], customer["food"])
                         for customer in customers]
    for customer in list_of_customers:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie, list_of_customers, Cleaner(cleaner))
