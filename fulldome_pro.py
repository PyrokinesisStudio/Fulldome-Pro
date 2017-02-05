# Copyright 2016 John Roper
#
# ##### BEGIN GPL LICENSE BLOCK ######
#
# Fulldome Pro is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Fulldome Pro is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Fulldome Pro.  If not, see <http://www.gnu.org/licenses/>.
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Fulldome Pro",
    "author": "John Roper",
    "version": (1, 0, 0),
    "blender": (2, 78, 0),
    "location": "3D View > Toolbar > Tools > Fulldome Pro",
    "description": "Quicly set up your scene for fulldome production",
    "warning": "",
    "wiki_url": "http://jmroper.com/",
    "tracker_url": "mailto:johnroper100@gmail.com",
    "category": "Render"
}

import bpy
import os
from bpy.types import Operator, Panel
from bpy.props import *


class FPSetupScene(Operator):
    """Setup a fulldome scene"""
    bl_idname = "scene.fp_setup_scene"
    bl_label = "Setup Fulldome Scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.scene.render.engine == "CYCLES":
            scene = bpy.context.scene
            main_quality = 4096
            if scene.FP_quality == 'high':
                scene.render.resolution_x = main_quality
                scene.render.resolution_y = main_quality
            elif scene.FP_quality == 'medium':
                scene.render.resolution_x = main_quality/2
                scene.render.resolution_y = main_quality/2
            elif scene.FP_quality == 'low':
                scene.render.resolution_x = main_quality/4
                scene.render.resolution_y = main_quality/4
            else:
                print("There is a problem with the quality variable. Did you try to enter a value other then high, medium, or low?")

            scene.render.resolution_percentage = 100

            cam = bpy.data.cameras.new("Fulldome Camera")
            cam.type = 'PANO'
            cam.cycles.panorama_type = 'FISHEYE_EQUIDISTANT'
            cam_ob = bpy.data.objects.new("Fulldome Camera", cam)
            cam_ob.rotation_euler = (1.5707963705062866, 0, 0)
            scene.objects.link(cam_ob)
            scene.camera = cam_ob
        else:
            self.report({'ERROR'}, "You must enable Cycles to use Fulldome Pro!")

        return {'FINISHED'}


class FPSetupPreview(Operator):
    """Setup a fulldome preview scene"""
    bl_idname = "scene.fp_setup_preview"
    bl_label = "Setup Fulldome Preview"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.scene.render.engine == "CYCLES":
            scene = bpy.context.scene
            context = bpy.context

            verts = [(0.3044823706150055, 1.5307337045669556, 7.846282005310059), (0.5972632765769958, 3.0026423931121826, 7.391036033630371), (0.8670915961265564, 4.359160900115967, 6.651756763458252), (1.1035979986190796, 5.548159122467041, 5.656854152679443), (1.2976939678192139, 6.523945331573486, 4.44456148147583), (1.4419200420379639, 7.249019145965576, 3.061467409133911), (1.5307341814041138, 7.695517539978027, 1.560722827911377), (1.560723066329956, 7.846282005310059, 6.039832101123466e-07), (0.5972636938095093, 1.4419195652008057, 7.846282005310059), (1.1715738773345947, 2.828427314758301, 7.391036033630371), (1.7008612155914307, 4.106239318847656, 6.651756763458252), (2.164785385131836, 5.226251125335693, 5.656854152679443), (2.545518159866333, 6.145421504974365, 4.44456148147583), (2.828427791595459, 6.828426361083984, 3.061467409133911), (3.00264310836792, 7.249018669128418, 1.560722827911377), (3.0614683628082275, 7.391035556793213, 6.039832101123466e-07), (0.8670925498008728, 1.2976930141448975, 7.846282005310059), (1.7008616924285889, 2.5455169677734375, 7.391036033630371), (2.4692676067352295, 3.6955175399780273, 6.651756763458252), (3.1427812576293945, 4.7035017013549805, 5.656854152679443), (3.69551944732666, 5.530733108520508, 4.44456148147583), (4.106240749359131, 6.145421028137207, 3.061467409133911), (4.359161853790283, 6.523943901062012, 1.560722827911377), (4.444563388824463, 6.6517558097839355, 6.039832101123466e-07), (1.1035994291305542, 1.103596806526184, 7.846282005310059), (2.1647863388061523, 2.1647837162017822, 7.391036033630371), (3.1427814960479736, 3.1427788734436035, 6.651756763458252), (4.000001430511475, 3.9999990463256836, 5.656854152679443), (4.7035040855407715, 4.703501224517822, 4.44456148147583), (5.226253032684326, 5.226250648498535, 3.061467409133911), (5.548160552978516, 5.548157691955566, 1.560722827911377), (5.656856060028076, 5.656852722167969, 6.039832101123466e-07), (1.297695517539978, 0.8670898675918579, 7.846282005310059), (2.5455193519592285, 1.7008591890335083, 7.391036033630371), (3.6955199241638184, 2.4692649841308594, 6.651756763458252), (4.7035040855407715, 3.1427783966064453, 5.656854152679443), (5.530735492706299, 3.695516586303711, 4.44456148147583), (6.145423412322998, 4.10623836517334, 3.061467409133911), (6.523946285247803, 4.359158515930176, 1.560722827911377), (6.651758670806885, 4.4445600509643555, 6.039832101123466e-07), (1.4419219493865967, 0.5972610116004944, 7.846282005310059), (2.8284294605255127, 1.1715713739395142, 7.391036033630371), (4.106241703033447, 1.7008585929870605, 6.651756763458252), (5.226253509521484, 2.1647825241088867, 5.656854152679443), (6.145423889160156, 2.5455150604248047, 4.44456148147583), (6.828428268432617, 2.828425407409668, 3.061467409133911), (7.249020099639893, 3.0026392936706543, 1.560722827911377), (7.391037940979004, 3.061465263366699, 6.039832101123466e-07), (1.5307360887527466, 0.304479718208313, 7.846282005310059), (3.0026445388793945, 0.597260594367981, 7.391036033630371), (4.3591628074646, 0.8670889139175415, 6.651756763458252), (5.548161029815674, 1.1035953760147095, 5.656854152679443), (6.523946762084961, 1.297690987586975, 4.44456148147583), (7.249020576477051, 1.4419176578521729, 3.061467409133911), (7.695518493652344, 1.5307307243347168, 1.560722827911377), (7.846283912658691, 1.5607199668884277, 6.039832101123466e-07), (1.5607248544692993, -2.6130874175578356e-06, 7.846282005310059), (3.061469554901123, -2.553482772782445e-06, 7.391036033630371), (4.444563865661621, -2.4938781280070543e-06, 6.651756763458252), (5.656855583190918, -2.553482772782445e-06, 5.656854152679443), (6.651758193969727, -2.672692062333226e-06, 4.44456148147583), (7.391037464141846, -2.195854904130101e-06, 3.061467409133911), (7.846282005310059, -3.149529220536351e-06, 1.560722827911377), (8.000001907348633, -3.03031993098557e-06, 6.039832101123466e-07), (1.530735969543457, -0.30448493361473083, 7.846282005310059), (3.0026443004608154, -0.5972656607627869, 7.391036033630371), (4.3591628074646, -0.8670939207077026, 6.651756763458252), (5.548160552978516, -1.103600263595581, 5.656854152679443), (6.523946285247803, -1.2976962327957153, 4.44456148147583), (7.249020576477051, -1.4419220685958862, 3.061467409133911), (7.695517539978027, -1.5307368040084839, 1.560722827911377), (7.846283912658691, -1.5607259273529053, 6.039832101123466e-07), (1.441921591758728, -0.5972661375999451, 7.846282005310059), (2.8284289836883545, -1.1715761423110962, 7.391036033630371), (4.106241226196289, -1.7008633613586426, 6.651756763458252), (5.226253032684326, -2.1647872924804688, 5.656854152679443), (6.145422458648682, -2.545520305633545, 4.44456148147583), (6.828428268432617, -2.828429698944092, 3.061467409133911), (7.249018669128418, -3.0026450157165527, 1.560722827911377), (7.391037464141846, -3.0614709854125977, 6.039832101123466e-07), (1.2976950407028198, -0.8670948147773743, 7.846282005310059), (2.5455188751220703, -1.7008635997772217, 7.391036033630371), (3.69551944732666, -2.4692695140838623, 6.651756763458252), (4.703503608703613, -3.142782688140869, 5.656854152679443), (5.530734062194824, -3.695521354675293, 4.44456148147583), (6.14542293548584, -4.1062421798706055, 3.061467409133911), (6.52394437789917, -4.359163284301758, 1.560722827911377), (6.651757717132568, -4.444565296173096, 6.039832101123466e-07), (1.1035988330841064, -1.1036015748977661, 7.846282005310059), (2.164785861968994, -2.164788007736206, 7.391036033630371), (3.1427807807922363, -3.1427831649780273, 6.651756763458252), (4.000000476837158, -4.000002861022949, 5.656854152679443), (4.703502178192139, -4.703505516052246, 4.44456148147583), (5.226253032684326, -5.226254463195801, 3.061467409133911), (5.548158645629883, -5.548161506652832, 1.560722827911377), (5.656854629516602, -5.656857967376709, 6.039832101123466e-07), (0.867091953754425, -1.2976975440979004, 7.846282005310059), (1.7008612155914307, -2.545520782470703, 7.391036033630371), (2.469266891479492, -3.695521354675293, 6.651756763458252), (3.142780065536499, -4.703505516052246, 5.656854152679443), (3.6955177783966064, -5.530736446380615, 4.44456148147583), (4.106240749359131, -6.145424842834473, 3.061467409133911), (4.35915994644165, -6.523947238922119, 1.560722827911377), (4.444561958312988, -6.651760578155518, 6.039832101123466e-07), (0.5972633361816406, -1.4419238567352295, 7.846282005310059), (1.1715736389160156, -2.828430652618408, 7.391036033630371), (1.7008607387542725, -4.106243133544922, 6.651756763458252), (2.1647841930389404, -5.226254463195801, 5.656854152679443), (2.5455164909362793, -6.1454243659973145, 4.44456148147583), (2.828427791595459, -6.828429698944092, 3.061467409133911), (3.002641201019287, -7.249021053314209, 1.560722827911377), (3.061467170715332, -7.391039848327637, 6.039832101123466e-07), (0.3044821619987488, -1.5307379961013794, 7.846282005310059), (0.5972632169723511, -3.00264573097229, 7.391036033630371), (0.8670914173126221, -4.359164237976074, 6.651756763458252), (1.1035972833633423, -5.54816198348999, 5.656854152679443), (1.2976925373077393, -6.523946762084961, 4.44456148147583), (1.4419201612472534, -7.249022006988525, 3.061467409133911), (1.5307328701019287, -7.69551944732666, 1.560722827911377), (1.56072199344635, -7.846285820007324, 6.039832101123466e-07), (-5.7696126987138996e-08, -1.5607267618179321, 7.846282005310059), (3.2973406405290007e-07, -3.0614707469940186, 7.391036033630371), (2.1052477450211882e-07, -4.444565296173096, 6.651756763458252), (-2.0670773892561556e-07, -5.656856536865234, 5.656854152679443), (-6.835448971287406e-07, -6.651757717132568, 4.44456148147583), (5.085479983790719e-07, -7.39103889465332, 3.061467409133911), (-6.835448971287406e-07, -7.846282958984375, 1.560722827911377), (-8.027541866795218e-07, -8.00000286102295, 6.039832101123466e-07), (-0.30448225140571594, -1.5307377576828003, 7.846282005310059), (-0.5972625017166138, -3.002645254135132, 7.391036033630371), (-0.8670909404754639, -4.359164237976074, 6.651756763458252), (-1.1035977602005005, -5.548161506652832, 5.656854152679443), (-1.2976938486099243, -6.5239458084106445, 4.44456148147583), (-1.441919207572937, -7.249022006988525, 3.061467409133911), (-1.5307340621948242, -7.695518493652344, 1.560722827911377), (-1.5607235431671143, -7.846284866333008, 6.039832101123466e-07), (-0.5972632765769958, -1.4419234991073608, 7.846282005310059), (-1.1715728044509888, -2.828429937362671, 7.391036033630371), (-1.7008602619171143, -4.106243133544922, 6.651756763458252), (-2.1647844314575195, -5.226253986358643, 5.656854152679443), (-2.5455172061920166, -6.145421981811523, 4.44456148147583), (-2.8284265995025635, -6.828429698944092, 3.061467409133911), (-3.0026421546936035, -7.249019622802734, 1.560722827911377), (-3.0614686012268066, -7.391038417816162, 6.039832101123466e-07), (-1.4482216101896483e-06, -4.774147328134859e-06, 8.0), (-0.8670917749404907, -1.2976970672607422, 7.846282005310059), (-1.7008601427078247, -2.5455198287963867, 7.391036033630371), (-2.469266414642334, -3.695521354675293, 6.651756763458252), (-3.14277982711792, -4.70350456237793, 5.656854152679443), (-3.6955175399780273, -5.530733585357666, 4.44456148147583), (-4.106239318847656, -6.1454243659973145, 3.061467409133911), (-4.359160423278809, -6.523945331573486, 1.560722827911377), (-4.444562911987305, -6.651758670806885, 6.039832101123466e-07), (-1.1035984754562378, -1.1036009788513184, 7.846282005310059), (-2.1647844314575195, -2.1647868156433105, 7.391036033630371), (-3.142780065536499, -3.1427829265594482, 6.651756763458252), (-4.0, -4.000001907348633, 5.656854152679443), (-4.703501224517822, -4.703502178192139, 4.44456148147583), (-5.226251125335693, -5.226253986358643, 3.061467409133911), (-5.548158168792725, -5.548159122467041, 1.560722827911377), (-5.65685510635376, -5.656855583190918, 6.039832101123466e-07), (-1.297694444656372, -0.8670942187309265, 7.846282005310059), (-2.5455172061920166, -1.7008624076843262, 7.391036033630371), (-3.6955182552337646, -2.469269037246704, 6.651756763458252), (-4.703502178192139, -3.1427817344665527, 5.656854152679443), (-5.530732154846191, -3.6955182552337646, 4.44456148147583), (-6.145421504974365, -4.1062421798706055, 3.061467409133911), (-6.5239434242248535, -4.359160423278809, 1.560722827911377), (-6.65175724029541, -4.444562911987305, 6.039832101123466e-07), (-1.4419207572937012, -0.5972656607627869, 7.846282005310059), (-2.8284268379211426, -1.1715749502182007, 7.391036033630371), (-4.1062397956848145, -1.7008626461029053, 6.651756763458252), (-5.226251602172852, -2.1647861003875732, 5.656854152679443), (-6.145419597625732, -2.5455174446105957, 4.44456148147583), (-6.828426837921143, -2.828429698944092, 3.061467409133911), (-7.249017238616943, -3.0026419162750244, 1.560722827911377), (-7.391036033630371, -3.0614683628082275, 6.039832101123466e-07), (-1.530734896659851, -0.30448460578918457, 7.846282005310059), (-3.0026416778564453, -0.59726482629776, 7.391036033630371), (-4.359160900115967, -0.8670933246612549, 6.651756763458252), (-5.548159122467041, -1.1035990715026855, 5.656854152679443), (-6.523942470550537, -1.2976939678192139, 4.44456148147583), (-7.249019145965576, -1.4419221878051758, 3.061467409133911), (-7.695515155792236, -1.5307339429855347, 1.560722827911377), (-7.8462815284729, -1.5607235431671143, 6.039832101123466e-07), (-1.5607236623764038, -2.4938781280070543e-06, 7.846282005310059), (-3.061466932296753, -2.255459548905492e-06, 7.391036033630371), (-4.44456148147583, -2.255459548905492e-06, 6.651756763458252), (-5.656853675842285, -1.4805991668254137e-06, 5.656854152679443), (-6.651753902435303, -1.12297129817307e-06, 4.44456148147583), (-7.391035556793213, -2.553482772782445e-06, 3.061467409133911), (-7.846278667449951, -7.653434295207262e-07, 1.560722827911377), (-7.999998569488525, -1.12297129817307e-06, 6.039832101123466e-07), (-1.5307347774505615, 0.30447956919670105, 7.846282005310059), (-3.0026416778564453, 0.5972602963447571, 7.391036033630371), (-4.359160423278809, 0.8670886754989624, 6.651756763458252), (-5.548158645629883, 1.1035959720611572, 5.656854152679443), (-6.523941516876221, 1.2976917028427124, 4.44456148147583), (-7.249018669128418, 1.441917061805725, 3.061467409133911), (-7.695513725280762, 1.530732274055481, 1.560722827911377), (-7.846280097961426, 1.5607212781906128, 6.039832101123466e-07), (-1.4419206380844116, 0.5972605347633362, 7.846282005310059), (-2.8284265995025635, 1.1715704202651978, 7.391036033630371), (-4.106238842010498, 1.7008578777313232, 6.651756763458252), (-5.226250648498535, 2.164782762527466, 5.656854152679443), (-6.145418167114258, 2.5455148220062256, 4.44456148147583), (-6.828426361083984, 2.8284244537353516, 3.061467409133911), (-7.249014854431152, 3.0026397705078125, 1.560722827911377), (-7.39103364944458, 3.0614657402038574, 6.039832101123466e-07), (-1.297694206237793, 0.867089033126831, 7.846282005310059), (-2.5455164909362793, 1.7008576393127441, 7.391036033630371), (-3.695517063140869, 2.469263792037964, 6.651756763458252), (-4.703501224517822, 3.142777919769287, 5.656854152679443), (-5.5307297706604, 3.6955151557922363, 4.44456148147583), (-6.145421028137207, 4.106236934661865, 3.061467409133911), (-6.523940563201904, 4.359157562255859, 1.560722827911377), (-6.651753902435303, 4.444559574127197, 6.039832101123466e-07), (-1.1035981178283691, 1.1035957336425781, 7.846282005310059), (-2.164783477783203, 2.1647815704345703, 7.391036033630371), (-3.1427786350250244, 3.14277720451355, 6.651756763458252), (-3.9999988079071045, 3.999997854232788, 5.656854152679443), (-4.703498363494873, 4.703498840332031, 4.44456148147583), (-5.226251125335693, 5.226248741149902, 3.061467409133911), (-5.548154830932617, 5.548154830932617, 1.560722827911377), (-5.656850814819336, 5.656851291656494, 6.039832101123466e-07), (-0.8670914173126221, 1.2976917028427124, 7.846282005310059), (-1.7008593082427979, 2.5455141067504883, 7.391036033630371), (-2.4692649841308594, 3.6955151557922363, 6.651756763458252), (-3.1427783966064453, 4.703499794006348, 5.656854152679443), (-3.695514440536499, 5.530729293823242, 4.44456148147583), (-4.106238842010498, 6.145418643951416, 3.061467409133911), (-4.359156608581543, 6.523939609527588, 1.560722827911377), (-4.444558620452881, 6.651752948760986, 6.039832101123466e-07), (-0.5972628593444824, 1.441918134689331, 7.846282005310059), (-1.1715720891952515, 2.8284239768981934, 7.391036033630371), (-1.7008590698242188, 4.106236457824707, 6.651756763458252), (-2.164783000946045, 5.2262492179870605, 5.656854152679443), (-2.54551362991333, 6.145416736602783, 4.44456148147583), (-2.8284263610839844, 6.828423500061035, 3.061467409133911), (-3.002638339996338, 7.2490129470825195, 1.560722827911377), (-3.061464309692383, 7.391031265258789, 6.039832101123466e-07), (-0.3044818043708801, 1.5307321548461914, 7.846282005310059), (-0.597261905670166, 3.002638816833496, 7.391036033630371), (-0.8670899271965027, 4.359157085418701, 6.651756763458252), (-1.1035962104797363, 5.548156261444092, 5.656854152679443), (-1.297690510749817, 6.52393913269043, 4.44456148147583), (-1.441918969154358, 7.249015808105469, 3.061467409133911), (-1.5307307243347168, 7.6955108642578125, 1.560722827911377), (-1.5607198476791382, 7.84627628326416, 6.039832101123466e-07), (2.9993174166520475e-07, 1.5607209205627441, 7.846282005310059), (6.277572879298532e-07, 3.0614638328552246, 7.391036033630371), (8.661758670314157e-07, 4.4445576667785645, 6.651756763458252), (1.2238037925271783e-06, 5.656850814819336, 5.656854152679443), (2.1774781089334283e-06, 6.651750087738037, 4.44456148147583), (5.085479983790719e-07, 7.3910322189331055, 3.061467409133911), (2.058268819382647e-06, 7.846274375915527, 1.560722827911377), (2.1774781089334283e-06, 7.999993324279785, 6.039832101123466e-07)]

            faces = [(249, 0, 144), (250, 1, 0, 249), (251, 2, 1, 250), (252, 3, 2, 251), (253, 4, 3, 252), (254, 5, 4, 253), (255, 6, 5, 254), (256, 7, 6, 255), (7, 15, 14, 6), (0, 8, 144), (1, 9, 8, 0), (2, 10, 9, 1), (3, 11, 10, 2), (4, 12, 11, 3), (5, 13, 12, 4), (6, 14, 13, 5), (11, 19, 18, 10), (12, 20, 19, 11), (13, 21, 20, 12), (14, 22, 21, 13), (15, 23, 22, 14), (8, 16, 144), (9, 17, 16, 8), (10, 18, 17, 9), (23, 31, 30, 22), (16, 24, 144), (17, 25, 24, 16), (18, 26, 25, 17), (19, 27, 26, 18), (20, 28, 27, 19), (21, 29, 28, 20), (22, 30, 29, 21), (28, 36, 35, 27), (29, 37, 36, 28), (30, 38, 37, 29), (31, 39, 38, 30), (24, 32, 144), (25, 33, 32, 24), (26, 34, 33, 25), (27, 35, 34, 26), (32, 40, 144), (33, 41, 40, 32), (34, 42, 41, 33), (35, 43, 42, 34), (36, 44, 43, 35), (37, 45, 44, 36), (38, 46, 45, 37), (39, 47, 46, 38), (44, 52, 51, 43), (45, 53, 52, 44), (46, 54, 53, 45), (47, 55, 54, 46), (40, 48, 144), (41, 49, 48, 40), (42, 50, 49, 41), (43, 51, 50, 42), (49, 57, 56, 48), (50, 58, 57, 49), (51, 59, 58, 50), (52, 60, 59, 51), (53, 61, 60, 52), (54, 62, 61, 53), (55, 63, 62, 54), (48, 56, 144), (61, 69, 68, 60), (62, 70, 69, 61), (63, 71, 70, 62), (56, 64, 144), (57, 65, 64, 56), (58, 66, 65, 57), (59, 67, 66, 58), (60, 68, 67, 59), (66, 74, 73, 65), (67, 75, 74, 66), (68, 76, 75, 67), (69, 77, 76, 68), (70, 78, 77, 69), (71, 79, 78, 70), (64, 72, 144), (65, 73, 72, 64), (78, 86, 85, 77), (79, 87, 86, 78), (72, 80, 144), (73, 81, 80, 72), (74, 82, 81, 73), (75, 83, 82, 74), (76, 84, 83, 75), (77, 85, 84, 76), (82, 90, 89, 81), (83, 91, 90, 82), (84, 92, 91, 83), (85, 93, 92, 84), (86, 94, 93, 85), (87, 95, 94, 86), (80, 88, 144), (81, 89, 88, 80), (94, 102, 101, 93), (95, 103, 102, 94), (88, 96, 144), (89, 97, 96, 88), (90, 98, 97, 89), (91, 99, 98, 90), (92, 100, 99, 91), (93, 101, 100, 92), (99, 107, 106, 98), (100, 108, 107, 99), (101, 109, 108, 100), (102, 110, 109, 101), (103, 111, 110, 102), (96, 104, 144), (97, 105, 104, 96), (98, 106, 105, 97), (111, 119, 118, 110), (104, 112, 144), (105, 113, 112, 104), (106, 114, 113, 105), (107, 115, 114, 106), (108, 116, 115, 107), (109, 117, 116, 108), (110, 118, 117, 109), (115, 123, 122, 114), (116, 124, 123, 115), (117, 125, 124, 116), (118, 126, 125, 117), (119, 127, 126, 118), (112, 120, 144), (113, 121, 120, 112), (114, 122, 121, 113), (127, 135, 134, 126), (120, 128, 144), (121, 129, 128, 120), (122, 130, 129, 121), (123, 131, 130, 122), (124, 132, 131, 123), (125, 133, 132, 124), (126, 134, 133, 125), (132, 140, 139, 131), (133, 141, 140, 132), (134, 142, 141, 133), (135, 143, 142, 134), (128, 136, 144), (129, 137, 136, 128), (130, 138, 137, 129), (131, 139, 138, 130), (137, 146, 145, 136), (138, 147, 146, 137), (139, 148, 147, 138), (140, 149, 148, 139), (141, 150, 149, 140), (142, 151, 150, 141), (143, 152, 151, 142), (136, 145, 144), (150, 158, 157, 149), (151, 159, 158, 150), (152, 160, 159, 151), (145, 153, 144), (146, 154, 153, 145), (147, 155, 154, 146), (148, 156, 155, 147), (149, 157, 156, 148), (154, 162, 161, 153), (155, 163, 162, 154), (156, 164, 163, 155), (157, 165, 164, 156), (158, 166, 165, 157), (159, 167, 166, 158), (160, 168, 167, 159), (153, 161, 144), (166, 174, 173, 165), (167, 175, 174, 166), (168, 176, 175, 167), (161, 169, 144), (162, 170, 169, 161), (163, 171, 170, 162), (164, 172, 171, 163), (165, 173, 172, 164), (171, 179, 178, 170), (172, 180, 179, 171), (173, 181, 180, 172), (174, 182, 181, 173), (175, 183, 182, 174), (176, 184, 183, 175), (169, 177, 144), (170, 178, 177, 169), (183, 191, 190, 182), (184, 192, 191, 183), (177, 185, 144), (178, 186, 185, 177), (179, 187, 186, 178), (180, 188, 187, 179), (181, 189, 188, 180), (182, 190, 189, 181), (187, 195, 194, 186), (188, 196, 195, 187), (189, 197, 196, 188), (190, 198, 197, 189), (191, 199, 198, 190), (192, 200, 199, 191), (185, 193, 144), (186, 194, 193, 185), (199, 207, 206, 198), (200, 208, 207, 199), (193, 201, 144), (194, 202, 201, 193), (195, 203, 202, 194), (196, 204, 203, 195), (197, 205, 204, 196), (198, 206, 205, 197), (204, 212, 211, 203), (205, 213, 212, 204), (206, 214, 213, 205), (207, 215, 214, 206), (208, 216, 215, 207), (201, 209, 144), (202, 210, 209, 201), (203, 211, 210, 202), (216, 224, 223, 215), (209, 217, 144), (210, 218, 217, 209), (211, 219, 218, 210), (212, 220, 219, 211), (213, 221, 220, 212), (214, 222, 221, 213), (215, 223, 222, 214), (221, 229, 228, 220), (222, 230, 229, 221), (223, 231, 230, 222), (224, 232, 231, 223), (217, 225, 144), (218, 226, 225, 217), (219, 227, 226, 218), (220, 228, 227, 219), (225, 233, 144), (226, 234, 233, 225), (227, 235, 234, 226), (228, 236, 235, 227), (229, 237, 236, 228), (230, 238, 237, 229), (231, 239, 238, 230), (232, 240, 239, 231), (237, 245, 244, 236), (238, 246, 245, 237), (239, 247, 246, 238), (240, 248, 247, 239), (233, 241, 144), (234, 242, 241, 233), (235, 243, 242, 234), (236, 244, 243, 235), (242, 250, 249, 241), (243, 251, 250, 242), (244, 252, 251, 243), (245, 253, 252, 244), (246, 254, 253, 245), (247, 255, 254, 246), (248, 256, 255, 247), (241, 249, 144)]

            mesh_data = bpy.data.meshes.new("cube_mesh_data")
            mesh_data.from_pydata(verts, [], faces)
            mesh_data.update()

            obj = bpy.data.objects.new("Dome Preview", mesh_data)

            scene.objects.link(obj)
            obj.select = True

            mat_name = "Fulldome Material"
            mat = (bpy.data.materials.get(mat_name) or bpy.data.materials.new(mat_name))
            mat.use_nodes = True
            tree = mat.node_tree
            nodes = tree.nodes
            links = tree.links

            for node in nodes:
                nodes.remove(node)

            node1 = nodes.new('ShaderNodeEmission')
            node1.location = 100, 0

            node2 = nodes.new('ShaderNodeOutputMaterial')
            node2.location = 0, 0

            previewImage = os.path.abspath(scene.FP_preview_image)
            image = bpy.data.images.load(previewImage, check_existing=True)

            node3 = nodes.new(type='ShaderNodeTexImage')
            node3.location = 200, 0
            node3.image = image

            link = links.new(node3.outputs[0], node1.inputs[0])
            link = links.new(node1.outputs[0], node2.inputs[0])

            if obj.data.materials:
                # assign to 1st material slot
                obj.data.materials[0] = mat
            else:
                # no slots
                obj.data.materials.append(mat)

            context.space_data.viewport_shade = 'MATERIAL'

            #for area in bpy.context.screen.areas:
             #   if area.type == 'VIEW_3D':
              #      for region in area.regions:
               #         if region.type == 'WINDOW':
                #            override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                 #           bpy.ops.uv.unwrap(override)

        else:
            self.report({'ERROR'}, "You must enable Cycles to use Fulldome Pro!")

        return {'FINISHED'}


class FPPanel(Panel):
    """Creates Fulldome Pro Panel in the tools panel."""
    bl_idname = "FPPanel"
    bl_label = "Fulldome Pro"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='MAT_SPHERE_SKY')

    def draw(self, context):
        scene = bpy.context.scene
        layout = self.layout

        if bpy.context.scene.render.engine == "CYCLES":
            row = layout.row()
            row.prop(scene, "FP_quality", icon='SETTINGS')

            row = layout.row()
            row.scale_y = 1.2
            row.operator("scene.fp_setup_scene", icon='FILE_TICK')

            row = layout.row()
            row.prop(scene, "FP_preview_image", icon='SETTINGS')

            row = layout.row()
            row.scale_y = 1.1
            row.operator("scene.fp_setup_preview", icon='IMAGE_COL')
        else:
            row = layout.row()
            row.label("You must enable Cycles to use Fulldome Pro!", icon='ERROR')


def register():
    bpy.utils.register_class(FPSetupScene)
    bpy.utils.register_class(FPSetupPreview)
    bpy.utils.register_class(FPPanel)
    bpy.types.Scene.FP_quality = bpy.props.EnumProperty(
        items=[('high', 'High', '4k image quality'),
               ('medium', 'Medium', '2k image quality'),
               ('low', 'Low', 'HD image quality')],
        name="Quality",
        description="The output image size",
        default="high")
    bpy.types.Scene.FP_preview_image = bpy.props.StringProperty (name="Assets Zip", default="", description="Define the assets zip file", subtype='FILE_PATH')


def unregister():
    bpy.utils.unregister_class(FPSetupScene)
    bpy.utils.unregister_class(FPSetupPreview)
    bpy.utils.unregister_class(FPPanel)

    del bpy.types.Scene.FP_quality
    del bpy.types.Scene.FP_preview_image


if __name__ == "__main__":
    register()
