from django.test import TestCase
from category.models import Region, Category, Brand

class CategoryModelTest(TestCase):
    def test_create_main_category(self):
        category = Category.objects.create(
            name="Electronic",
            is_main=True,
            slug="electronic",
        )
        self.assertEqual(category.name, "Electronic")
        self.assertTrue(category.is_main)
        self.assertEqual(category.slug, "electronic")
        self.assertIsNone(category.parent)

    def test_create_subcategory(self):
        parent = Category.objects.create(name="Electronic", is_main=True, slug="electronic")
        sub = Category.objects.create(
            name="Telefonlar",
            slug="telefonlar",
            parent=parent
        )
        self.assertEqual(sub.name, "Telefonlar")
        self.assertEqual(sub.parent, parent)
class RegionModelTest(TestCase):
    def test_create_region(self):
        region =Region.objects.create(name="Toshkent", sorting=1)
        self.assertEqual(region.name, "Toshkent")
        self.assertEqual(region.sorting, 1)

class BrandModelTest(TestCase):
    def test_create_brand(self):
        brand = Brand.objects.create(name="Samsung")
        self.assertEqual(brand.name, "Samsung")


