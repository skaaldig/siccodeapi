from django.db import models


class MajorGroup(models.Model):
    """
    First two digits in the SICCODE
    """
    major_number = models.CharField(max_length=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.major_number} - {self.description}'


class IndustryGroup(models.Model):
    """
    Third digit in SICCODE
    """
    major_number = models.ForeignKey(MajorGroup, on_delete=models.CASCADE)
    group_number = models.CharField(max_length=1)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.group_number} - {self.description}'


class IndustrySector(models.Model):
    """
    Fourth digit in SICCODE
    """
    group_number = models.ForeignKey(IndustryGroup, on_delete=models.CASCADE)
    sector_number = models.CharField(max_length=1)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.sector_number} - {self.description}'


class SicCode(models.Model):
    """
    Full 4 digit SICCODE
    """
    major_group = models.ForeignKey(MajorGroup, on_delete=models.CASCADE)
    industry_group = models.ForeignKey(IndustryGroup, on_delete=models.CASCADE)
    industry_sector = models.ForeignKey(IndustrySector, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    sic_code = models.CharField(max_length=4, blank=True)

    def save(self):
        group = self.major_group
        industry = self.industry_group
        sector = self.industry_sector

        self.sic_code = group.major_number + industry.group_number + sector.sector_number
        self.description = sector.description
        super(SicCode, self).save()

    def __str__(self):
        return f'{self.sic_code} - {self.description}'
