from pickle import FALSE

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Patient Master"

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    tag_ids = fields.Many2many("patient.tag", "patient_tag_rel","patient_id","tag_id",string="Tags", tracking=True)

    # def unlink(self):
    #
    #     for rec in self:
    #         domain = [('patient_id', '=',rec.id)]
    #         appointments = self.env['hospital.appointment'].search(domain)
    #
    #         if appointments:
    #             raise ValidationError(_("You cannot delete this record because appointment exist"))
    #
    #     print("Super method is executed")
    #     return super().unlink()
    @api.ondelete(at_uninstall=False)
    def _check_patient_appointments(self):
        try:
            for rec in self:
                # Define the domain to search for related appointments
                domain = [('patient_id', '=', rec.id)]
                appointments = self.env['hospital.appointment'].search(domain)

                # If appointments are found, raise a ValidationError to prevent deletion
                if appointments:
                    raise UserError(_("You cannot delete this record because appointments existing for this patient: %s" % rec.name))

            # If no appointments exist, proceed with the deletion
            print("Super method is executed")
            return super().unlink()

        except UserError as e:
            # Handle the validation error (if raised)
            print(f"ValidationError: {e}")
            raise e  # Re-raise the error after logging or handling it if needed

        except Exception as e:
            # Handle any other unexpected errors
            print(f"Unexpected error occurred: {e}")
            raise UserError(_("An unexpected error occurred during deletion. Please try again later."))