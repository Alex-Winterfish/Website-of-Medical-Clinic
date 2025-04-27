from django.db import models

class MedStaffModel(models.Model):
    '''Модель медицинского специалиста model:clinic.model.MedStaffModel.'''

    MD = 'Врач'
    NURSE = 'Медсестра'

    TITLE_IN_CHOICES = [
        (MD, 'Врач'),
        (NURSE, 'Медсестра')
    ]

    GYNECOLOGIST = 'гинеколог'
    CARDIOLOGIST = 'кардиолог'
    NEUROSURGEON = 'нейрохирург'
    NEUROLOGIST = 'невролог'
    ENDOCRINOLOGIST = 'эндокринолог'
    THERAPIST = 'терапевт'
    ONCOLOGIST = 'онколог'
    RHEUMATOLOGIST = 'ревматолог'
    PHLEBOLOGIST = 'флеболог'
    MAMMOLOG = 'мамолог'
    RADIOLOGIST = 'рентгенолог'

    SPECIALITY_IN_CHOICES = [
        (GYNECOLOGIST, 'гинеколог'),
        (CARDIOLOGIST, 'кардиолог'),
        (NEUROSURGEON, 'нейрохирург'),
        (NEUROLOGIST, 'невролог'),
        (ENDOCRINOLOGIST, 'эндокринолог'),
        (THERAPIST, 'терапевт'),
        (ONCOLOGIST, 'онколог'),
        (RHEUMATOLOGIST, 'ревматолог'),
        (PHLEBOLOGIST, 'флеболог'),
        (MAMMOLOG, 'мамолог'),
        (RADIOLOGIST, 'рентгенолог')
    ]

    name = models.CharField(max_length=1000, verbose_name='Ф.И.О медицинского специалиста.')
    title = models.CharField(choices=TITLE_IN_CHOICES, verbose_name='медицинская должность')
    speciality = models.CharField(choices=SPECIALITY_IN_CHOICES, verbose_name='специальность')

    def __str__(self):
        if self.title == self.MD:
            return f'{self.name}: {self.title}-{self.speciality}.'
        else:
            return f'{self.name}: {self.title}.'

    class Meta:
        verbose_name = 'Медицинский работник'
        verbose_name_plural = 'Медицинские работники'

class MedServiceModel(models.Model):
    '''Модель медицинской услуги model:clinic.models.MedServiceModel.'''

    name = models.CharField(max_length=1000, verbose_name='название медицинской услуги')
    description = models.CharField(max_length=2000, verbose_name='описание медицинской услуги')

    def __str__(self):
        return f'Медицинская услуга: {self.name}.'

    class Meta:
        verbose_name = 'Медицинская услуга'
        verbose_name_plural = 'Медицинские услуги'

class AppointmentModel(models.Model):
    '''Модель запись на медицинскую услугу model:clinic.models.AppointmentModel.'''

    ap_date = models.DateTimeField(verbose_name='дата и время оказания медицинской услуги.')
    med_spec = models.ForeignKey('clinic.MedStaffModel', on_delete=models.SET_NULL, verbose_name='назначенный медицинский специалист')
    med_serv = models.ForeignKey('clinic.MedServiceModel', on_delete=models.CASCADE, verbose_name='медицинская услуга')
    patient = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='пациент')

    def __str__(self):
        return f'Запись на {self.med_serv.name}. Дата: {self.ap_date}.'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'


class ResultModel(models.Model):
    '''Модель результат диагностики model:clinic.models.ResultModel.'''
    result_date = models.DateField(verbose_name='дата результата медуслуги')
    appointment = models.ForeignKey('clinic.AppointmentModel', on_delete=models.SET_NULL)
    result = models.TextField(max_length=5000, verbose_name='эпикриз по результатам медицинской процедуры')

    def __str__(self):
        return f'Результаты процедуры от {self.result_date}.'

    class Meta:
        verbose_name = 'результат'
        verbose_name_plural = 'результаты'



