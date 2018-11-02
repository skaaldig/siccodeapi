import uuid
from django.db import models


class CommonInfo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class IndustrySector(CommonInfo):
    """
    First two digits in the SICCODE
    """
    sector_id = models.CharField(max_length=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.sector_id} - {self.description}'


class IndustryGroup(CommonInfo):
    """
    Third digit in SICCODE
    """
    sector_id = models.ForeignKey(IndustrySector, on_delete=models.CASCADE)
    group_id = models.CharField(max_length=1)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.group_id} - {self.description}'


class Industry(CommonInfo):
    """
    Fourth digit in SICCODE
    """
    group_id = models.ForeignKey(IndustryGroup, on_delete=models.CASCADE)
    industry_id = models.CharField(max_length=1)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.industry_id} - {self.description}'


class SicCode(CommonInfo):
    """
    Full 4 digit SICCODE
    """
    sector_id = models.ForeignKey(IndustrySector, on_delete=models.CASCADE)
    group_id = models.ForeignKey(IndustryGroup, on_delete=models.CASCADE)
    industry_id = models.ForeignKey(Industry, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    sic_code = models.CharField(max_length=4, blank=True)

    def save(self):
        sector = self.sector_id
        group = self.group_id
        industry = self.industry_id

        self.sic_code = sector.sector_id + group.group_id + industry.industry_id
        self.description = industry.description
        super(SicCode, self).save()

    def __str__(self):
        return f'{self.sic_code} - {self.description}'
