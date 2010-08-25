import json
import logging
import re

from wufoo import core

class Forms(core.ListResource):
    """ A list of Form resources """

    def __init__(self, uri, **kwargs):
        name = "Forms"
        uri += "/forms"
        super(Forms, self).__init__(uri, name=name, **kwargs)

    def _load_instance(self, d):
        return Form(self.uri, client=self.client, entries=d)

class Form(core.InstanceResource):
    """ A Form resource """

    def __init__(self, uri, entries={}, **kwargs):
        if "Hash" not in entries:
            raise core.WufooException, "Hash Identifier Missing"
        uri += "/" + entries["Hash"]
        
        self.fields  = Fields(uri, **kwargs)
        self.entries = Entries(uri, **kwargs)

        super(Form, self).__init__(uri, entries=entries, **kwargs)

class Reports(core.ListResource):
    """ A list of Report resources """

    def __init__(self, uri, **kwargs):
        name = "Reports"
        uri += "/reports"
        super(Reports, self).__init__(uri, name=name, **kwargs)

    def _load_instance(self, d):
        return Report(self.uri, entries=d, client=self.client)

class Report(core.InstanceResource):
    """ A Report resource """

    def __init__(self, uri, entries={}, **kwargs):
        if "Hash" not in entries:
            raise core.WufooException, "Hash Identifier Missing"
        uri += "/" + entries["Hash"]
        
        self.entries = Entries(uri, **kwargs)
        self.fields  = Fields(uri, **kwargs)
        self.widgets = Widgets(uri, **kwargs)

        super(Report, self).__init__(uri, entries=entries, **kwargs)

class Users(core.ListResource):
    """ A list of User resources """

    def __init__(self, uri, **kwargs):
        name = "Users"
        uri += "/users"
        super(Users, self).__init__(uri, name=name, **kwargs)

    def _load_instance(self, d):
        return User(self.uri, client=self.client, entries=d)

class User(core.InstanceResource):
    """ A User resource """

    def __init__(self, uri, entries={}, **kwargs):
        if "Hash" not in entries:
            raise core.WufooException, "Hash Identifier Missing"
        uri += "/" + entries["Hash"]
        
        super(User, self).__init__(uri, entries=entries, **kwargs)

class Fields(core.ListResource):
    """ A Wufoo Fields resource """

    DEFAULT_FIELDS = ['UpdatedBy', 'LastUpdated', 'CreatedBy', 
                      'DateCreated', 'EntryId']

    def __init__(self, uri, **kwargs):
        name = "Fields"
        uri += "/fields"
        super(Fields, self).__init__(uri, name=name, **kwargs)

    def _load_instance(self, d):
        if "ID" in d and d["ID"] in self.DEFAULT_FIELDS:
            return None

        return Field(self.uri, client=self.client, entries=d)

class Field(core.InstanceResource):
    """ A Field resource """

    def __init__(self, uri, entries={}, **kwargs):
        super(Field, self).__init__(uri, entries=entries, **kwargs)


class Widgets(core.ListResource):
    """ A Wufoo Widgets resource """

    def __init__(self, uri, **kwargs):
        name = "Widgets"
        uri += "/widgets"
        super(Widgets, self).__init__(uri, name=name, **kwargs)

    def _load_instance(self, d):
        return Widget(self.uri, client=self.client, entries=d)

class Entries(core.ListResource):
    """ A Wufoo Entries resource """

    def __init__(self, uri, **kwargs):
        name = "Entries"
        uri += "/entries"
        super(Entries, self).__init__(uri, name=name, **kwargs)

    def _load_instance(self, d):
        return Entry(self.uri, client=self.client, entries=d)

    def count(self):
        """ Return the total number of entries in this resource """
        content = json.loads(self._get("/count"))
        return content["EntryCount"]

 



