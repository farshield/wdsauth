from flask import render_template, redirect, url_for, request, flash
from wdsauth.epicenter import epicenter
from models import Static, Wormhole
from forms import SystemSearchForm


@epicenter.route('/systeminfo')
def systeminfo():
    if request.args.get('jcode', None):
        jcode = request.args['jcode']
        return redirect(url_for('epicenter.systeminfo_jcode', jcode=jcode))

    return render_template('systeminfo.html')


@epicenter.route('/systeminfo/<jcode>')
def systeminfo_jcode(jcode):
    wh = Wormhole.query.filter_by(system_name=jcode.upper()).first()
    return render_template('systeminfo.html', jcode=jcode, wh=wh)


@epicenter.route('/statics')
def statics():
    static_list = Static.query.order_by(Static.code).all()
    return render_template('statics.html', static_list=static_list)

@epicenter.route('/systemsearch')
def systemsearch():
    form = SystemSearchForm()
    return render_template('systemsearch.html', form=form)
