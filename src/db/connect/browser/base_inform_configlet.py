# -*- coding: utf-8 -*-
from db.connect import _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from zope import schema
from plone.z3cform import layout
from z3c.form import form
from plone.directives import form as Form


class IInform(Form.Schema):

    rate = schema.Float(
        title=_(u'Bonus rate'),
        required=False
    )

class BasicInformControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IInform

CustomControlPanelView = layout.wrap_form(BasicInformControlPanelForm, ControlPanelFormWrapper)
CustomControlPanelView.label = _(u"Basic Inform")
