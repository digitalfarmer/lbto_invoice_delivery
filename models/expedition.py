from odoo import api, fields, models

class InvoiceDelivery(models.Model):
    _name = 'invoice.delivery'
    _description = 'InvoiceDelivery for expedition'

    name = fields.Char('No Lembar Ekspedisi')
    delivery_date = fields.Date('Tanggal')
    personal_code = fields.Char('Kode Personil')
    vehicle_number = fields.Char('No Kendaraan')
    odometer_start= fields.Integer('KM Berangkat')
    odometer_finish = fields.Integer('KM Kembali')
    time_receive = fields.Datetime('Waktu Terima')
    time_go = fields.Datetime('Waktu Berangkat')
    time_back = fields.Datetime('Waktu kembali')
    state_deliver = fields.Selection([
        ('cancel','Batal'),
        ('back', 'Kembali'),
        ('pending', 'Pending'),
        ('sent', 'Kirim'),
        ('receive', 'Terima'),
    ], default="pending")
    expedition_lines= fields.One2many('invoice.delivery.detail','expedition_id','Ekspedisi Detail')

class InvoiceDeliveryDetail(models.Model):
    _name = 'invoice.delivery.detail'
    _description = 'InvoiceDeliveryDetail'

    name = fields.Many2one('invoice.delivery', 'Ekspedisi')
    # sequence_number_next= fields.Many2one('account.invoice','No Faktur')
    invoice_number = fields.Char('No Faktur')
    notes= fields.Text()
    state_invoice = fields.Selection([
        ('back', 'Kembali'),
        ('pending', 'Pending'),
        ('sent', 'Kirim'),
        ('receive', 'Terima'),
    ], default="pending")
    receive_date= fields.Date()
    expedition_id= fields.Many2one('invoice.delivery', 'Ekspedisi')