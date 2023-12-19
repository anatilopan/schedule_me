from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.sql import func
from app import db
from datetime import datetime, timezone

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return f'<User {self.username}'

class periods(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(120))
    description: so.Mapped[str] = so.mapped_column(sa.String(250))
    created_at: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    start_date: so.Mapped[datetime] = so.mapped_column(sa.DateTime())
    end_date: so.Mapped[datetime] = so.mapped_column(sa.DateTime())
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    created_by: so.Mapped[User] = so.relationship(back_populates='periods')

    def __repr__(self):
        return f'<Period {name}>'