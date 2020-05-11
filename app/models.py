from app import db
from datetime import datetime, timedelta


class EPI(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    cnpj_cpf = db.Column(db.Integer, nullable=False)
    observacao = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def teste(self):
        return (datetime.now() - self.created_at).days

    def ultimo_15(self):
        return (datetime.now() - self.created_at).days < 15

    @property
    def qt_ultimo_15_dias(self):
        return EPI.query.filter(
            EPI.cnpj_cpf == self.cnpj_cpf,
            EPI.created_at >= (datetime.now()-timedelta(days=15))
        ).count()


class Profissional(db.Model):

    __bind_key__ = 'sgh'
    __tablename__ = 'TBUSERS'

    nome = db.Column(db.String(31), primary_key=True)
    nomec = db.Column(db.String(70))
    cpf = db.Column(db.Integer)
