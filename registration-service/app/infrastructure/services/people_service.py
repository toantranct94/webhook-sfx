from app.infrastructure.databases import db
from app.infrastructure.models import People


class PeopleService:

    def get_people_by_id(self, people_id: int):
        people = People.query.get(people_id)
        return people

    def get_people_by_email(self, email: str):
        people = People.query.filter_by(email=email).first()
        return people

    def create_people(self, email: str, role: str):
        people = People(email=email, role=role)
        db.session.add(people)
        db.session.commit()
        return people

    def update_people(self, people_id: int, role: str):
        people = People.query.get(people_id)
        people.role = role
        db.session.commit()
        return people

    def delete_people(self, people_id: int):
        people = People.query.get(people_id)
        db.session.delete(people)
        db.session.commit()
        return people
