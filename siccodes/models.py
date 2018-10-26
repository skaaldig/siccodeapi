from django.db import models


class SicDescription(models.Model):
    description = models.CharField(max_length=255)

    class Meta:
        abstract = True


class MajorGroup(SicDescription):
    """
    First two digits in the SICCODE
    """
    major_number = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.major_number}  {self.description}'


class IndustryGroup(SicDescription):
    """
    Third digit in SICCODE
    """
    major_number = models.ForeignKey(MajorGroup, on_delete=models.CASCADE)
    group_number = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.group_number}  {self.description}'


class IndustrySector(SicDescription):
    """
    Fourth digit in SICCODE
    """
    group_number = models.ForeignKey(IndustryGroup, on_delete=models.CASCADE)
    sector_number = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.sector_number}  {self.description}'


class SicCode(SicDescription):
    """
    Full 4 digit SICCODE
    """
    major_group = models.ForeignKey(MajorGroup, on_delete=models.CASCADE)
    industry_group = models.ForeignKey(IndustryGroup, on_delete=models.CASCADE)
    industry_sector = models.ForeignKey(IndustrySector, on_delete=models.CASCADE)
    sic_code = models.CharField(max_length=4)

    def save(self):
        group = self.major_group
        industry = self.industry_group
        sector = self.industry_sector

        self.sic_code = group.major_number + industry.group_number + sector.sector_number
        self.description = sector.description
        super(SicCode, self).save()
