from django.db import models


class IndustrySector(models.Model):
    """
    First two digits in the SICCODE
    """
    industry_sector = models.CharField(max_length=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.industry_sector} - {self.description}'


class IndustryGroup(models.Model):
    """
    Third digit in SICCODE
    """
    industry_sector = models.ForeignKey(IndustrySector, on_delete=models.CASCADE)
    industry_group = models.CharField(max_length=1)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.industry_group} - {self.description}'


class Industry(models.Model):
    """
    Fourth digit in SICCODE
    """
    industry_group = models.ForeignKey(IndustryGroup, on_delete=models.CASCADE)
    industry = models.CharField(max_length=1)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.industry} - {self.description}'


class SicCode(models.Model):
    """
    Full 4 digit SICCODE
    """
    industry_sector = models.ForeignKey(IndustrySector, on_delete=models.CASCADE)
    industry_group = models.ForeignKey(IndustryGroup, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    sic_code = models.CharField(max_length=4, blank=True)

    def save(self):
        sector = self.industry_sector
        group = self.industry_group
        industry_num = self.industry

        self.sic_code = sector.industry_sector + group.industry_group + industry_num.industry
        self.description = industry_num.description
        super(SicCode, self).save()

    def __str__(self):
        return f'{self.sic_code} - {self.description}'
