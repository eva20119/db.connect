# -*- coding: utf-8 -*-
from db.connect import _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from zope import schema
from plone.z3cform import layout
from z3c.form import form
from zope.interface import Interface


class IInform(Interface):

    email = schema.TextLine(
        title=_(u'email'),
        required=False,
    )
    cellphone = schema.TextLine(
        title=_(u'cellphone'),
        required=False,
    )
    address = schema.TextLine(
        title=_(u'address'),
        required=False
    )
    fax = schema.TextLine(
        title=_(u'fax'),
        required=False
    )

class BasicInformControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IInform

CustomControlPanelView = layout.wrap_form(BasicInformControlPanelForm, ControlPanelFormWrapper)
CustomControlPanelView.label = _(u"Basic Inform")
