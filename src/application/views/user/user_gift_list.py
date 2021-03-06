from flask.views import View

from flask import flash
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask import request

from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from google.appengine.ext import ndb

from models import GiftModel
from models import UserModel
from forms import GiftForm

from decorators import registration_required


class UserGifts(View):
    @registration_required
    def dispatch_request(self, user_id):
        user_key = ndb.Key(UserModel, user_id)
        gift_list = GiftModel.query(GiftModel.owner == user_key)
        #owner = UserModel.get_by_id(user_id)

        registered_users = UserModel.query().order(UserModel.user_last_name)
        households = list(set([x.user_household for x in registered_users]))
        owner = filter(lambda x: x.key.id()==user_id, registered_users)[0]

        form = GiftForm()
        if form.validate_on_submit():
            auth = ndb.Key(UserModel, session['user']['uid'])
            gift = GiftModel(
                owner=user_key,
                added_by=auth,
                summary=form.summary.data,
                description=form.description.data,
                notes=form.notes.data
            )
            try:
                gift.put()
                gift_id = gift.key.id()
                flash(u'Item successfully added to gift list.', 'success')
                return redirect(url_for('gift_list', user_id=user_id))
            except CapabilityDisabledError:
                flash(u'App Engine Datastore is currently in read-only mode.', 'info')
                return redirect(url_for('gift_list', user_id=user_id))

        return render_template(
            'list_gifts.html',
            gifts=gift_list,
            form=form,
            auth=session.get('user', {}),
            owner=owner,
            households=households
        )
