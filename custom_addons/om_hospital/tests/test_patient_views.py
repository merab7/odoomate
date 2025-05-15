from odoo.tests.common import TransactionCase, tagged
from odoo.exceptions import ValidationError

@tagged('post_install', '-at_install')
class TestPatientViews(TransactionCase):

    def setUp(self):
        super().setUp()
        # Create test data
        self.patient = self.env['hospital.patient'].create({
            'name': 'Test Patient',
            'date_of_birth': '1990-01-01',
            'gender': 'male',
        })

    def test_create_patient(self):
        """Test patient creation with basic fields"""
        self.assertEqual(self.patient.name, 'Test Patient')
        self.assertEqual(self.patient.gender, 'male')
        self.assertEqual(str(self.patient.date_of_birth), '1990-01-01')
        self.assertFalse(self.patient.is_minor)

    def test_patient_tags(self):
        """Test adding tags to a patient"""
        tag = self.env['patient.tag'].create({'name': 'Test Tag'})
        self.patient.write({'tag_ids': [(4, tag.id)]})
        self.assertEqual(len(self.patient.tag_ids), 1)
        self.assertEqual(self.patient.tag_ids[0].name, 'Test Tag')

    def test_patient_deletion_with_appointment(self):
        """Test patient deletion restriction when linked to appointment"""
        # Create an appointment for the patient
        appointment = self.env['hospital.appointment'].create({
            'patient_id': self.patient.id,
            'appointment_date': '2024-03-20',
        })

        # Try to delete the patient - should raise ValidationError
        with self.assertRaises(ValidationError):
            self.patient.unlink()

    def test_patient_deletion_without_appointment(self):
        """Test patient deletion when not linked to any appointment"""
        # Create a new patient without appointments
        new_patient = self.env['hospital.patient'].create({
            'name': 'Delete Test Patient',
            'date_of_birth': '1995-01-01',
            'gender': 'female',
        })
        
        # Should be able to delete without error
        new_patient.unlink()
        # Verify patient is deleted
        self.assertFalse(self.env['hospital.patient'].search([('id', '=', new_patient.id)]))

    def test_minor_patient_guardian(self):
        """Test minor patient guardian field behavior"""
        minor_patient = self.env['hospital.patient'].create({
            'name': 'Minor Patient',
            'date_of_birth': '2020-01-01',
            'gender': 'female',
            'is_minor': True,
            'guardian': 'John Doe'
        })
        
        self.assertTrue(minor_patient.is_minor)
        self.assertEqual(minor_patient.guardian, 'John Doe')