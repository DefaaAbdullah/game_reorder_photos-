import webbrowser
import os
import re
# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>REORDER PHOTOS LIKE STRING</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Drag&amp;Drop Reorder</title>
<link href="css/style.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="js/jquery-1.8.3.min.js"></script>
<script type="text/javascript" src="js/jquery-ui.js"></script>
<script type="text/javascript">
$(document).ready(function(){
    $('.reorder_link').on('click',function(){
        $("ul.reorder-photos-list").sortable({ tolerance: 'pointer' });
        $('.image_link').attr("href","javascript:void(0);");
        $('.image_link').css("cursor","move");
        $("#save_reorder").click(function( e ){
            if( !$("#save_reorder i").length )
            {
                $("ul.reorder-photos-list").sortable('destroy');
                var h = [];
                $("ul.reorder-photos-list li").each(function() {  h.push($(this).attr('id').substr(9));  });
            }   
            e.preventDefault();     
        });
    });
    
});
</script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

 <div style="margin-top:50px;">
    <a href="javascript:void(0);" class="btn outlined mleft_no reorder_link" id="save_reorder">reorder photos Start</a>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">GAME REORDER PHOTOS</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {photos_tiles}
    </div>
  </body>
</html>
'''


# ALL PHOTOS entry html template
photos_tile_content = '''
    <div class="gallery" id="REORDER_PHOTOS">
     <div class="container"> 
    <h3 style="padding:0px;">{STRING_PHOTOS}</h3>
    </div>
        <ul class="reorder_ul reorder-photos-list">
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img1.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img2.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img3.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img4.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img5.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img6.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img7.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img8.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img9.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img10.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img11.jpg" alt=""></a></li>
            <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img12.jpg" alt=""></a></li>
             <li id="image_li_1" class="ui-sortable-handle"><a href="javascript:void(0);" style="float:none;" class="image_link"><img src="images/img13.jpg" alt=""></a></li>
        </ul>
    </div>

'''


def create_photos_tiles_content(photos):
    # The HTML content for this section of the page
    content = ''
    for photos in photos:
        # Append the tile for the REORDER PHOTOS with its content filled in
        content += photos_tile_content.format(
            STRING_PHOTOS = photos.STRING_PHOTOS
        )
    return content


def open_photos_page(photos):
    # Create or overwrite the output file
    output_file = open('Simple_game.html', 'w')

    # Replace the REORDER PHOTOS tiles placeholder generated content
    rendered_content = main_page_content.format(
        photos_tiles=create_photos_tiles_content(photos))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)