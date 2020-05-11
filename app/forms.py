from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired


class EPIForm(FlaskForm):
    epi_cnpj_cpf = HiddenField('CPF', validators=[DataRequired()])
    epi_profissional = HiddenField('Profissional')
    epi_observacao = TextAreaField('Justificativa para um novo lançamento (Obrigatório)', validators=[DataRequired()])
    epi_submit = SubmitField('Salvar')


class SearchForm(FlaskForm):
    search_cnpj_cpf = StringField('CPF', validators=[DataRequired()])
    search_submit = SubmitField('Lançar')
