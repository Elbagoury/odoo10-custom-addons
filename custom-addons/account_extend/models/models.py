from odoo import models, fields, api
from odoo.exceptions import Warning, ValidationError

class account_extend(models.Model):
	_inherit = 'account.invoice'

	bill_no     = fields.Char(string="Bill No")
	frm_bill_no = fields.Char(string="From Bill No")
	province    = fields.Char(string="Province")
	branch      = fields.Many2one('branch',string="Branch")
	bill_num    = fields.Char(string="To Bill No")
	m_tons      = fields.Float(string="M Tons")
	# summary_id  = fields.Many2one('summary.ffc')

# ==================punching branch in account.move on validate button using fun super========
# ==================punching branch in account.move on validate button using fun super========

	@api.multi
	def action_invoice_open(self):
		new_record = super(account_extend, self).action_invoice_open()
		JournalEntry =  self.env['account.move'].search([('name','=',self.number)])
		if self.branch:
			JournalEntry.branch = self.branch.id

		return new_record


class move_extend(models.Model):
    _inherit = 'account.move'

    branch      = fields.Many2one('branch',string="Branch")


class journal_extend(models.Model):
    _inherit = 'account.journal'

    branch      = fields.Many2one('branch',string="Branch")


class bank_extend(models.Model):
	_inherit = 'account.bank.statement'

	branch      = fields.Many2one('branch',string="Branch")

# ===================showing branch of relevant journal in cash book==========================
# ===================showing branch of relevant journal in cash book==========================

	@api.onchange('journal_id')
	def get_branch(self):
		records = self.env['account.journal'].search([('id','=',self.journal_id.id)])
		self.branch = records.branch.id

	@api.multi
	def unlink(self):
		users = self.env['res.users'].search([('id','=',self._uid)])
		if users.name != "Administrator":
			raise  ValidationError('Cannot Delete Record')
	
		return super(bank_extend,self).unlink()


class bank_extend_line(models.Model):
	_inherit = 'account.bank.statement.line'

	branch   = fields.Many2one('branch',string="Branch")

# =========================punching branch in journal enteries using fun super===============
# =========================punching branch in journal enteries using fun super===============

	@api.multi
	def process_reconciliation(self,data,uid,id):
		new_record = super(bank_extend_line, self).process_reconciliation(data,uid,id)
		records = self.env['account.bank.statement'].search([('id','=',self.statement_id.id)])
		journal_entery =  self.env['account.move'].search([], order='id desc', limit=1)
		journal_entery.branch = records.branch.id
		return new_record



class ufc_user_extend(models.Model):
    _inherit  = 'res.users'
    Branch = fields.Many2one ('branch',string="Branch")



class branch(models.Model):
    _name = 'branch'

    Address = fields.Char(string="Address")
    name = fields.Char(string="Name")
    Phone = fields.Char(string="Phone")
    Mobile = fields.Char(string="Mobile")
    ptcl = fields.Char("Ptcl")

