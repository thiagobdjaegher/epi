from flask import Blueprint, render_template, flash, url_for, redirect
from app.models import EPI, Profissional
from app.forms import SearchForm, EPIForm

bl_epis = Blueprint('bl_epis', __name__)


@bl_epis.route('/', methods=['GET', 'POST'])
def main():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        profissional = Profissional.query.filter_by(cpf=search_form.search_cnpj_cpf.data).first()
        if profissional:
            epi = EPI.query.filter_by(cnpj_cpf=search_form.search_cnpj_cpf.data).order_by(EPI.created_at.desc()).first()
            if epi and epi.ultimo_15():
                epi_form = EPIForm()
                epi_form.epi_cnpj_cpf.data = profissional.cpf
                epi_form.epi_profissional.data = profissional.nomec
                return render_template('epis.html',
                                       search_form=search_form, epi_form=epi_form, profissional=profissional, epi=epi)
            else:
                new_epi(profissional.nome, search_form.search_cnpj_cpf.data)
                return redirect(url_for("bl_epis.main"))
        else:
            flash('CPF não cadastrado', 'alert alert-danger')
    return render_template('epis.html', search_form=search_form)


@bl_epis.route('/new_lan', methods=['POST'])
def new_lan():
    epi_form = EPIForm()
    if epi_form.validate_on_submit():
        new_epi(epi_form.epi_profissional.data, epi_form.epi_cnpj_cpf.data, epi_form.epi_observacao.data)
    return redirect(url_for("bl_epis.main"), code=307)


def new_epi(profissional, cnpj_cpf, observacao=''):
    epi = EPI(
        cnpj_cpf=cnpj_cpf,
        observacao=observacao
    )
    epi.commit()
    flash('N95 lançada com sucesso para '+profissional, 'alert alert-success')
