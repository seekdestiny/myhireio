from django import forms

class CompanyForm(forms.Form):
    name = forms.CharField(
        label='Company name',
        max_length=50,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'company_post_text_area company_function',
            'text-length': 50,
        }),
    )
    tag_name = forms.CharField(
        label='Company tag',
        max_length=100,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'company_post_text_area company_function',
            'text-length': 100,
        }),
    )
    product = forms.CharField(
        label='Product',
        max_length=1500,
        required=True,
            widget=forms.Textarea(attrs={
            'class': 'company_post_text_area company_function',
            'text-length': 1500,
        }),)
    why_us = forms.CharField(
        label='Why us',
        max_length=1500,
        required=False,
           widget=forms.Textarea(attrs={
            'class': 'company_post_text_area company_function',
            'text-length': 1500,
        }),
    )
    traction = forms.CharField(
        label='Tranction',
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'company_post_text_area company_function',
            'text-length': 500,
        }),
    )
    funding = forms.CharField(
        label='Funding',
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'company_post_text_area company_function',
            'text-length': 500,
        }),
    )
    size = forms.CharField(
        label='Company size',
        required=True,
    )
    market = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'company_post_text_area company_function',
            'text-length': 100,
        }),
    )
    company_link = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'company_post_text_area company_function',
            'text-length': 50,
        }),
    )

class JobPostForm(forms.Form):
    company = forms.CharField(
        label='Company name',
        max_length=50,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area job_function',
            'text-length': 50,
        }),
    )
    description = forms.CharField(
        label='Description',
        max_length=1500,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area description',
            'text-length': 1500,
        }),
    )
    requirements = forms.CharField(
        label='Requirements',
        max_length=1500,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area requirements',
            'text-length': 1500,
        }),
    )
    skills = forms.CharField(label='Skills needed',
        max_length=500,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area skills',
            'text-length': 500,
        }),
    )
    location = forms.CharField(
        label='Location',
        max_length=100,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area location',
            'text-length': 100,
        }),
    )
    salary = forms.CharField(
        label='Base salary',
        max_length=50,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area salary',
            'text-length': 50,
        }),
    )
    equity = forms.CharField(
        label='Equity',
        max_length=50,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area equity',
            'text-length': 50,
        }),
    )
    job_type = forms.CharField(
        label='Type',
        max_length=20,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area job_type',
            'text-length': 20,
        }),
    )
    job_title = forms.CharField(
        label='Title',
        max_length=30,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area job_title',
            'text-length': 30,
        }),
    )
    responsibility = forms.CharField(
        label='Responsibility',
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'job_post_text_area job_function',
            'text-length': 1000,
        }),
    )

class PerksForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=30,
        required=True,
    )

    description = forms.CharField(
        label='description',
        max_length=100,
        required=True,
    )
