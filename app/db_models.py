from enum import unique
from typing import List
from typing import Optional
from jinja2.nodes import For
from sqlalchemy import ForeignKey
from sqlalchemy import String, BigInteger, Integer, Boolean, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    enc_password: Mapped[str] = mapped_column(String(50))
    salt: Mapped[str] = mapped_column(String(50))


class Result(Base):
    __tablename__ = "results"
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    Id: Mapped[int] = mapped_column(primary_key=True)
    Naziv: Mapped[str] = mapped_column(String(255))
    Adresa: Mapped[str] = mapped_column(String(255))
    Telefon: Mapped[str] = mapped_column(String(255))
    GodisnjiPrihodi: Mapped[int] = mapped_column(BigInteger)
    BrojZaposlenih: Mapped[int] = mapped_column(Integer)
    FinansijskiPZ: Mapped[bool] = mapped_column(Boolean)
    FinansijskiPK: Mapped[bool] = mapped_column(Boolean)
    LicniPK: Mapped[bool] = mapped_column(Boolean)
    MedicinskiPK: Mapped[bool] = mapped_column(Boolean)
    DeljenjePK: Mapped[bool] = mapped_column(Boolean)
    Websajt: Mapped[bool] = mapped_column(Boolean)
    BrojJavnihURL: Mapped[int] = mapped_column(Integer)
    PolitikaPrivatnosti: Mapped[bool] = mapped_column(Boolean)
    PolitikaZadrzavanjaIBrisanja: Mapped[bool] = mapped_column(Boolean)
    BezbednosniTestovi: Mapped[bool] = mapped_column(Boolean)
    PlanReagovanjaNaIncident: Mapped[bool] = mapped_column(Boolean)
    PlanOporavka: Mapped[bool] = mapped_column(Boolean)
    KreiranjeRezervnihKopija: Mapped[bool] = mapped_column(Boolean)

    BezbednoSkladistenjePodataka: Mapped[bool] = mapped_column(Boolean)
    ObukaIB: Mapped[bool] = mapped_column(Boolean)
    ZakonPOLPP: Mapped[bool] = mapped_column(Boolean)
    Pcidss: Mapped[bool] = mapped_column(Boolean)
    Iso27001: Mapped[bool] = mapped_column(Boolean)
    ZeljeniIznosNaknade: Mapped[int] = mapped_column(Integer)
    BrojIncidenata: Mapped[int] = mapped_column(Integer)
    Factor = relationship("Factor", backref='result', uselist=False)
    SelectedItem = relationship("SelectedItem", back_populates="Result")


class Factor(Base):
    __tablename__ = "factors"
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    Id: Mapped[int] = mapped_column(primary_key=True)
    BaznaPremija: Mapped[int] = mapped_column(BigInteger)
    Factor1: Mapped[float] = mapped_column(Float)
    Factor2: Mapped[float] = mapped_column(Float)
    Factor3: Mapped[float] = mapped_column(Float)
    Factor4: Mapped[float] = mapped_column(Float)
    Factor5: Mapped[float] = mapped_column(Float)
    Factor6: Mapped[float] = mapped_column(Float)
    ResultId: Mapped[Result] = mapped_column(ForeignKey("results.Id"), unique=True)
    Result = relationship("Result", back_populates="Factor")


class CheckedItem(Base):
    __tablename__ = "checked_items"
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    Id: Mapped[str] = mapped_column(String(255), primary_key=True)
    Text: Mapped[String] = mapped_column(String(255))
    SelectedItem = relationship("SelectedItem", back_populates="CheckedItem")


class SelectedItem(Base):
    __tablename__ = "selected_items"
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    Id: Mapped[int] = mapped_column(primary_key=True)
    CheckedItemId: Mapped[str] = mapped_column(ForeignKey("checked_items.Id"))
    CheckedItem = relationship("CheckedItem", back_populates="SelectedItem")
    ResultId: Mapped[int] = mapped_column(ForeignKey("results.Id"))
    Result = relationship("Result", back_populates="SelectedItem")
