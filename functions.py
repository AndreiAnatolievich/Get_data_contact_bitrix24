def update_gender(bx, id, gen):
    params = {
        'ID': id,
        "fields":
        {'UF_CRM_GENDER': gen}
    }
    gender = bx.call('crm.contact.update', params)
    return gender