# pulpo-forms-examples

This project gives an overview of the finished product. To use it you need install the Pulpo Forms module with pip.

```
  pip install pulpo-forms
```

After you install de app, it's requirements, set up the database and run the migrations, run ``python manage.py loaddata pulpodata.json`` to get pre created forms with data to explore.

You can log with the superuser ``pulpo`` with password ``pulpo123``

* The application dashboard is in ``<base_url>/pulpo/``
* A sample form with model field (Combo box field where the options are django models instances) can be accessed through ``<base_url>/model_field_form/``
