from pyramid.events import subscriber
from websauna.system.crud.views import TraverseLinkButton
from pyramid.events import BeforeRender
from websauna.system.user.admins import UserAdmin


@subscriber(BeforeRender)
def contribute_admin(event):
    """Add notebook entry to the admin user interface."""

    # XXX: dummy way of adding button on context
    if not isinstance(event.get('context'), UserAdmin.Resource):
        return
    view = event.get('view')
    if view is None or not hasattr(view, 'resource_buttons'):
        return
    if "shell" in [i.id for i in event['view'].resource_buttons]:
        return
    button = TraverseLinkButton(
        id="shell",
        name="Shell",
        view_name="shell",
        permission="shell",
        tooltip="Open IPython Notebook shell and have this item prepopulated in obj variable.")
    event['view'].resource_buttons.append(button)
