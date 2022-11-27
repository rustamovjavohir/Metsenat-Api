from django.db import models


class Donate(models.Model):
    sponsor = models.ForeignKey('sponsors.SponsorWallet', on_delete=models.CASCADE, null=True,
                                related_name="sponsor_donate")
    student = models.ForeignKey('students.StudentWallet', on_delete=models.CASCADE, null=True,
                                related_name="student_wallet")
    donate = models.FloatField(default=0.0, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.donate
