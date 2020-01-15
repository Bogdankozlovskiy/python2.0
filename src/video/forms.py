from django import forms
from video.models import Comment, MyVideo


class CommentForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	text.widget.attrs.update({'class':'form-control'})

	def save(self, user_id, video_id):
		if self.is_valid():
			Comment.objects.create(
				text = self.cleaned_data['text'],
				user_id = user_id,
				video_id = video_id
			)
			return True
		return False

class VideoForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	description = forms.CharField(widget=forms.Textarea)
	url = forms.URLField()

	title.widget.attrs.update({'class':'form-control'})
	slug.widget.attrs.update({'class':'form-control'})
	description.widget.attrs.update({'class':'form-control'})
	url.widget.attrs.update({'class':'form-control'})

	def save(self):
		if self.is_valid():
			MyVideo.objects.create(
				title = self.cleaned_data['title'],
				slug = self.cleaned_data['slug'],
				description = self.cleaned_data['description'],
				url = self.cleaned_data['url'])
			return True
		return False


class NeEbstisVideo(forms.ModelForm):
	# title = forms.CharField()
	# slug = forms.SlugField()
	# description = forms.CharField(widget=forms.Textarea)
	# url = forms.URLField()

	# title.widget.attrs.update({'class':'form-control'})
	# slug.widget.attrs.update({'class':'form-control'})
	# description.widget.attrs.update({'class':'form-control'})
	# url.widget.attrs.update({'class':'form-control'})

	class Meta:
		model = MyVideo
		fields = ["title", "slug", "description", "url"]
		widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
		 			 "slug": forms.TextInput(attrs={'class':'form-control'}),
		 			 "description":forms.Textarea(attrs={'class':'form-control'}),
		 			 "url":forms.TextInput(attrs={'class':'form-control'})
		 			 }
