import os
import requests

# https://www.heirsholdings.com/wp-content/plugins/content-views-query-and-display-post-page/public/assets/css/cv.css    /assets/css/cv.css
# https://www.heirsholdings.com/wp-content/plugins/pt-content-views-pro/public/assets/css/cvpro.min.css  /assets/css/cvpro.min.css
# "https://www.heirsholdings.com/wp-includes/css/dashicons.min.css", /assets/css/dashicons.min.css
#    "https://www.heirsholdings.com/wp-content/plugins/post-views-counter/css/frontend.min.css", /assets/css/frontend1.min.css
#    "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/font-awesome.min.css", /assets/css/font-awesome.min.css
#    "https://www.heirsholdings.com/wp-content/plugins/tf-header-footer/assets/css/tf-style.css", /assets/css/tf-style.css
#     "https://www.heirsholdings.com/wp-content/plugins/cookie-notice/css/front.min.css" "/assets/css/front.min.css",
#    "/assets/css/timelentor.css", "https://www.heirsholdings.com/wp-content/plugins/timelentor/assets/css/timelentor.css"
#    "/assets/css/slick.css",  "https://www.heirsholdings.com/wp-content/plugins/timelentor/assets/css/slick.css"
    
#    "/assets/css/slick-theme.css", "https://www.heirsholdings.com/wp-content/plugins/timelentor/assets/css/slick-theme.css"
#    "/assets/css/ivory-search.min.css", "https://www.heirsholdings.com/wp-content/plugins/add-search-to-menu/public/css/ivory-search.min.css"
#    "/assets/css/frontend.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/frontend.min.css"
#    "/assets/css/widget-image.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-image.min.css"
#    "/assets/css/widget-nav-menu.min.css", "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/widget-nav-menu.min.css"

#    "/assets/css/sticky.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/modules/sticky.min.css"
#    "/assets/css/motion-fx.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/modules/motion-fx.min.css"
#    "/assets/css/widget-search-form.min.css", "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/widget-search-form.min.css"
#    "/assets/css/fontawesome.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/fontawesome.min.css"
#    "/assets/css/solid.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/solid.min.css"
#    "/assets/css/elementor-icons.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/eicons/css/elementor-icons.min.css"
#    "/assets/css/post-6013.css", "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-6013.css"
#    "/assets/css/all.min.css", "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/all.min.css"
#    "/assets/css/v4-shims.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/v4-shims.min.css"
#    "/assets/css/widget-heading.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-heading.min.css"
#    "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-icon-list.min.css",
#    "/assets/css/widget-share-buttons.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/widget-share-buttons.min.css"
#    "/assets/css/apple-webkit.min.css", "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/conditionals/apple-webkit.min.css"
#    "/assets/css/brands.min.css", "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/brands.min.css"
#    "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/widget-call-to-action.min.css",
#    "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/conditionals/transitions.min.css",
#    "/assets/css/fadeInUp.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/animations/styles/fadeInUp.min.css"
#     "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-spacer.min.css",
#     "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-video.min.css",
#     "/assets/css/widget-form.min.css",  "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/widget-form.min.css"
#     "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-24324.css",
#     "/assets/css/post-31.css", "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-31.css"
#     "/assets/css/post-48.css", "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-48.css"
#     "/assets/css/normalize.css",  "https://www.heirsholdings.com/wp-content/themes/disha/css/third-party/normalize.css"
#     "/assets/css/magnific-popup.css",  "https://www.heirsholdings.com/wp-content/themes/disha/css/third-party/magnific-popup.css"
#     "/assets/css/grid.css",  "https://www.heirsholdings.com/wp-content/themes/disha/css/grid.css"
#     "/assets/css/theme-icons.css", "https://www.heirsholdings.com/wp-content/themes/disha/css/font-icons/theme-icons/theme-icons.css"
#     "/assets/css/style.css",  "https://www.heirsholdings.com/wp-content/themes/disha/style.css"
#     "/assets/css/elements.css",  "https://www.heirsholdings.com/wp-content/themes/disha/css/elements.css"
#    "https://at.alicdn.com/t/font_o5hd5vvqpoqiwwmi.css"
#    "https://www.heirsholdings.com/wp-content/themes/disha/css/third-party/slick.css",  "/assets/css/slick1.css"
#     "https://www.heirsholdings.com/wp-content/themes/disha/css/third-party/slick-theme.css", "/assets/css/slick-theme1.css"
    # "/assets/css/ytprefs.min.css" "https://www.heirsholdings.com/wp-content/plugins/youtube-embed-plus/styles/ytprefs.min.css"

# "https://www.heirsholdings.com/wp-content/themes/heirsholdings/style.css" "/assets/css/style1.css"


# "https://www.heirsholdings.com/wp-includes/js/jquery/jquery.min.js"  "/assets/js/jquery.min.js",
# "https://www.heirsholdings.com/wp-includes/js/jquery/jquery-migrate.min.js"  "/assets/js/jquery-migrate.min.js",
# "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/font-awesome/js/v4-shims.min.js"  "/assets/js/v4-shims.min.js",
# "https://www.heirsholdings.com/wp-content/plugins/youtube-embed-plus/scripts/ytprefs.min.js"  "/assets/js/ytprefs.min.js"
 # "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.ttf",
    # "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.woff",
    # "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.svg",
    # "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/eicons/fonts/eicons.eot",
    # "https://www.heirsholdings.com/wp-content/uploads/2019/02/century-gothic-bold.ttf" "/assets/webfonts/century-gothic-bold.ttf",
    # "https://www.heirsholdings.com/wp-content/uploads/2019/06/search-alt.svg" "/assets/image/search-alt.svg"
#    "https://www.heirsholdings.com/wp-content/plugins/translatepress-multilingual/assets/css/.././assets/images/arrow-down-3101.svg" "/assets/image/arrow-down-3101.svg",
#    "https://www.heirsholdings.com/wp-content/uploads/2019/09/hh-arrow-right.svg"   "/assets/image/hh-arrow-right.svg"

    # "https://www.heirsholdings.com/wp-includes/css/dist/block-library/style.min.css" "/assets/css/style.min.css",
    # "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/widget-post-info.min.css" "/assets/css/widget-post-info.min.css",
    # "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/regular.min.css" "/assets/css/regular.min.css",
    # "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/widget-post-navigation.min.css" "/assets/css/widget-post-navigation.min.css",
    # "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/widget-posts.min.css" "/assets/css/widget-posts.min.css",
    # "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-883.css" "/assets/css/post-883.css",
    # "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/animations/styles/slideInUp.min.css"  "/assets/css/slideInUp.min.css",
    # "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/animations/styles/e-animation-grow.min.css" "/assets/css/e-animation-grow.min.css", 
    # "/assets/css/post-8.css"
#     "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-25189.css" "/assets/css/post-25189.css",
# "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-divider.min.css" "/assets/css/widget-divider.min.css",
# "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-social-icons.min.css" "/assets/css/widget-social-icons.min.css",
# "https://www.heirsholdings.com/wp-content/plugins/add-search-to-menu/public/css/ivory-ajax-search.min.css"  "/assets/css/ivory-ajax-search.min.css"
# "https://www.heirsholdings.com/wp-content/plugins/tf-header-footer/assets/js/svg-injector.min.js" "/assets/js/svg-injector.min.js",
#     "https://www.heirsholdings.com/wp-content/plugins/tf-header-footer/assets/js/tf-main.js" "/assets/js/tf-main.js",
#     "https://www.heirsholdings.com/wp-content/plugins/cookie-notice/js/front.min.js" "/assets/js/front.min.js",
#     "https://www.heirsholdings.com/wp-content/plugins/timelentor/assets/js/tmle-custom.js" "/assets/js/tmle-custom.js",
#     "https://www.heirsholdings.com/wp-content/plugins/timelentor/assets/js/slick.js" "/assets/js/slick.js",


#     "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/js/webpack.runtime.min.js" "/assets/js/webpack.runtime.min.js",
#     "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/js/frontend-modules.min.js" "/assets/js/frontend-modules.min.js",
#     "https://www.heirsholdings.com/wp-includes/js/jquery/ui/core.min.js" "/assets/js/core.min.js"
 
    # "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-google_maps.min.css" "/assets/css/widget-google_maps.min.css",
    # "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-14.css" "/assets/css/post-14.css"
     # "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-10.css"  "/assets/css/post-10.css"
    #  "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/js/frontend.min.js"  "/assets/js/frontend.min.js",
#  "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/lib/smartmenus/jquery.smartmenus.min.js"  "/assets/js/jquery.smartmenus.min.js",
#      "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/lib/sticky/jquery.sticky.min.js"  "/assets/js/jquery.sticky.min.js",
#   "https://www.heirsholdings.com/wp-content/plugins/content-views-query-and-display-post-page/public/assets/js/cv.js"   "/assets/js/cv.js",
#   "https://www.heirsholdings.com/wp-content/plugins/pt-content-views-pro/public/assets/js/cvpro.min.js"   "/assets/js/cvpro.min.js",
#   "https://www.heirsholdings.com/wp-content/plugins/add-search-to-menu/public/js/ivory-search.min.js"   "/assets/js/ivory-search.min.js",
#   "https://www.heirsholdings.com/wp-content/uploads/ac_assets/ue_ajax_search/ue_ajax_search.js"   "/assets/js/ue_ajax_search.js",
#    "https://www.heirsholdings.com/wp-content/uploads/ac_assets/uc_box_counter/jquery.waypoints.min.js"  "/assets/js/jquery.waypoints.min.js",
#     "https://www.heirsholdings.com/wp-content/uploads/ac_assets/uc_box_counter/counterup2.min.js"  "/assets/js/counterup2.min.js",
#   "https://www.heirsholdings.com/wp-content/themes/disha/js/plugins/modernizr.min.js"   "/assets/js/modernizr.min.js",
#     "https://www.heirsholdings.com/wp-content/themes/disha/js/plugins/lazysizes.min.js" "/assets/js/lazysizes.min.js",
#     "https://www.heirsholdings.com/wp-content/themes/disha/js/plugins/slick.min.js"  "/assets/js/slick.min.js",
#     "https://www.heirsholdings.com/wp-content/themes/disha/js/plugins/jquery.magnific-popup.min.js"  "/assets/js/jquery.magnific-popup.min.js",
#     "https://www.heirsholdings.com/wp-content/themes/disha/js/disha-core.min.js"  "/assets/js/disha-core.min.js",
#     "https://www.heirsholdings.com/wp-content/plugins/add-search-to-menu/public/js/ivory-ajax-search.min.js"  "/assets/js/ivory-ajax-search.min.js",
#     "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/js/webpack-pro.runtime.min.js"  "/assets/js/webpack-pro.runtime.min.js",
#    "https://www.heirsholdings.com/wp-includes/js/dist/hooks.min.js"  "/assets/js/hooks.min.js",
#     "https://www.heirsholdings.com/wp-includes/js/dist/i18n.min.js"  "/assets/js/i18n.min.js",
    
#    "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/js/elements-handlers.min.js"   "/assets/js/elements-handlers.min.js"
#  "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/js/frontend.min.js"  "/assets/js/frontend1.min.js"
#   "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-3459.css" "/assets/css/post-3459.css"
# "https://www.heirsholdings.com/wp-content/plugins/youtube-embed-plus/scripts/fitvids.min.js" "/assets/js/fitvids.min.js" 
#  "https://www.heirsholdings.com/wp-includes/js/imagesloaded.min.js" "/assets/js/imagesloaded.min.js"
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-11.css"  "/assets/css/post-11.css" 
#  "/assets/css/post-4419.css"

# "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/share-link/share-link.min.js" "/assets/js/share-link.min.js",
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-4421.css"  /assets/css/post-4421.css

# "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-toggle.min.css" "/assets/css/widget-toggle.min.css",
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-16318.css" "/assets/css/post-16318.css"

# "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-text-editor.min.css"  "/assets/css/widget-text-editor.min.css",
# "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/conditionals/popup.min.css"   "/assets/css/popup.min.css",
# "https://www.heirsholdings.com/wp-content/plugins/elementor-pro/assets/css/widget-search.min.css"  "/assets/css/widget-search.min.css",
# "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-tabs.min.css"  "/assets/css/widget-tabs.min.css",
# "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/lib/animations/styles/fadeIn.min.css"   "/assets/css/fadeIn.min.css",
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-13.css"  "/assets/css/post-13.css",
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-10390.css"  "/assets/css/post-10390.css",
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-25904.css"  "/assets/css/post-25904.css"
#   "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-4850.css" "/assets/css/post-4850.css"
# "https://www.heirsholdings.com/wp-content/plugins/add-search-to-menu/public/images/spinner.gif" "/assets/image/spinner.gif",
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-3492.css"  "/assets/css/post-3492.css",
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-3478.css"  "/assets/css/post-3478.css",
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-5571.css" "/assets/css/post-5571.css",
# "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-16647.css"   "/assets/css/post-16647.css"




urls = [
"/assets/css/widget-accordion.min.css", "https://www.heirsholdings.com/wp-content/plugins/elementor/assets/css/widget-accordion.min.css"
"/assets/css/post-12.css", "https://www.heirsholdings.com/wp-content/uploads/elementor/css/post-12.css"
];

output_dir = "assets"
os.makedirs(output_dir, exist_ok=True)

for url in urls:
    filename = url.split("/")
    newFilename = filename[-1]
    # print(output_dir + filename[-2])
    # filename = url.split("/")[-1].split(".")
    # filename[0]= filename[0] +"1"
    # newFilename = ".".join(filename)
    print(newFilename)
    filepath = os.path.join(output_dir + "/css", newFilename)

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"Downloaded: {filename}")

print("All files downloaded ✅")
# python assets/download.py

#011944 main color

# /assets/image/QTLobby.png
# /assets/image/QTLobby.png
# /assets/image/QBoardtoom.png