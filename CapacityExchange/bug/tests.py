from django.test import TestCase
from django.urls import reverse
from .models import Bug
from .forms import BugForm

# Create your tests here.
# This class contains tests for the Bug model
class BugModelTest(TestCase):
    def test_bug_model(self):
        bug = Bug(
            description="Test bug description",
            bug_type="Test Type",
            report_date="2023-10-05",
            status="Open"
        )
        bug.save()
        self.assertEqual(Bug.objects.count(), 1)
        self.assertEqual(str(bug), "Test bug description")

# This class contains tests for the Bug app's views
class BugViewsTest(TestCase):
    def setUp(self):
        self.bug = Bug.objects.create(
            description="Test bug description",
            bug_type="Test Type",
            report_date="2023-10-05",
            status="Open"
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/home.html')

    def test_register_bug_view(self):
        response = self.client.get(reverse('register_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/register_bug.html')

    def test_view_bug_view(self):
        response = self.client.get(reverse('view_bug', args=[self.bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/view_bug.html')

    def test_bug_list_view(self):
        response = self.client.get(reverse('bug_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/bug_list.html')
        self.assertContains(response, "Test bug description")
