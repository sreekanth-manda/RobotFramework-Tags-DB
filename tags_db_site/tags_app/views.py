from django.shortcuts import render, get_object_or_404
from .models import Tags, Releases


# tags_db_site views go here
def main_page(request):
    return render(request, "base.html")

def tagging_main_page(request):
    tag_types_list = Tags.objects.values_list('TagType', flat=True).distinct()
    return render(request, "home.html", {'tag_types_list':tag_types_list})

def get_tag_list(request, tag_starts_with):
    if tag_starts_with == "all":
        tag_list = Tags.objects.all()
    else:
        tag_types_list = Tags.objects.values_list('TagType', flat=True).distinct()
        tag_list = Tags.objects.filter(TagName__istartswith=tag_starts_with).exclude(TagType__contains='Testcase')
        #tag_list = Tags.objects.exclude(TagName__istartswith=tag_starts_with, TagType__contains='Testcase')
    return render(request, "tag_listing.html", {'starts_with':tag_starts_with,
                                                'tag_list':tag_list,
                                                'alphabet':tag_starts_with,
                                                'tag_types_list':tag_types_list})

def select_tags(request, tag_starts_with):
    release_list = Releases.objects.all()
    if tag_starts_with == "all":
        tag_list = Tags.objects.all()
    else:
        tag_list = Tags.objects.filter(TagName__istartswith=tag_starts_with).\
                        exclude(TagType__contains='Testcase').distinct()
    return render(request, "select_tags.html", {'release_list':release_list,
                                                'starts_with':tag_starts_with,
                                                'tag_list':tag_list})

def get_tags_info(request, tagName):
    print tagName
    if tagName == "all":
        tags = Tags.objects.all()
    else:
        tags = Tags.objects.filter(TagName__istartswith=tagName).distinct()
    return render(request, "tag_info.html", {'tags':tags})