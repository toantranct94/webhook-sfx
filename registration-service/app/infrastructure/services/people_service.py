from infrastructure.databases import db
from infrastructure.models import People


class PeopleService:
    """
    Service class for managing people.
    """

    def get_people_by_id(self, people_id: int):
        """
        Retrieve a person by their ID.

        Args:
            people_id (int): The ID of the person.

        Returns:
            People: The person object.
        """
        people = People.query.get(people_id)
        return people

    def get_people_by_email(self, email: str):
        """
        Retrieve a person by their email.

        Args:
            email (str): The email of the person.

        Returns:
            People: The person object.
        """
        people = People.query.filter_by(email=email).first()
        return people

    def create_people(self, email: str, role: str):
        """
        Create a new person.

        Args:
            email (str): The email of the person.
            role (str): The role of the person.

        Returns:
            People: The created person object.
        """
        people = People(email=email, role=role)
        db.session.add(people)
        db.session.commit()
        return people

    def update_people(self, people_id: int, role: str):
        """
        Update the role of a person.

        Args:
            people_id (int): The ID of the person.
            role (str): The new role of the person.

        Returns:
            People: The updated person object.
        """
        people = People.query.get(people_id)
        people.role = role
        db.session.commit()
        return people

    def delete_people(self, people_id: int):
        """
        Delete a person.

        Args:
            people_id (int): The ID of the person to delete.

        Returns:
            People: The deleted person object.
        """
        people = People.query.get(people_id)
        db.session.delete(people)
        db.session.commit()
        return people
