import bpy
import os
import math as m

bpy.ops.object.delete(use_global=False)

bpy.ops.object.lamp_add(type='SPOT', view_align=False,
                        location=(-15, 12, 35),
                        layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False, False))
bpy.ops.transform.trackball(value=(-0.57, -0.19), mirror=False, proportional='DISABLED',
                            proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True,
                            use_accurate=False)

bpy.ops.transform.rotate(value=0.549487, axis=(0, 0, 1), constraint_axis=(False, False, True),
                         constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                         proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True,
                         use_accurate=False)

bpy.ops.object.lamp_add(type='SPOT', view_align=False, location=(15, 0, 35), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False, False))
bpy.ops.transform.rotate(value=6.60845, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)


file_loc = '/home/ravil/Загрузки/1.obj'
imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
_dir = '/home/ravil/Загрузки/dir1'
#_x_turn = int(input('Введите в градусах разворот по оси х: '))
_step_degrees = 0
_step_ = 1

    
obj_object = bpy.context.selected_objects[0] #
_lamp_coord = bpy.data.objects['Lamp'].location
_lamp_coord[2] = 3.5   

bpy.ops.transform.resize(value=(0.025, 0.025, 0.025), constraint_axis=(True, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.object.shade_smooth()

bpy.ops.transform.rotate(value=-3.19073, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.rotate(value=0, axis=(-0.651558, 0.61417, -0.445271), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.rotate(value=-0.522564, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.rotate(value=1.63558, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.rotate(value=-0.498726, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.translate(value=(0, 0, 2.32357), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.translate(value=(0, 1.34821, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.translate(value=(0.680386, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.rotate(value=0.237416, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.translate(value=(0, 0, 0.487386), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.translate(value=(0, 0, -0.654753), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

bpy.ops.transform.rotate(value=-0.14388, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)



while True: 
    bpy.ops.transform.rotate(value=-m.radians(_step_degrees), axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    _lamp_coord[0] =  8
    _lamp_coord[1] = -6
    _photos = 'photo' + str(_step_)
    _main_catalogist = os.path.join(_dir, _photos)
    bpy.data.scenes["Scene"].render.filepath = _main_catalogist
    bpy.ops.render.render(write_still=True)
    _step_degrees += 0.0125
    _step_ += 1
    if _step_ == 201: break

    _lamp_coord[0] =  7.5
    _lamp_coord[1] = -6.5
    _photos = 'photo' + str(_step_)
    _main_catalogist = os.path.join(_dir, _photos)
    bpy.data.scenes["Scene"].render.filepath = _main_catalogist
    bpy.ops.render.render(write_still=True)
    _step_degrees += 0.0125
    _step_ += 1
    if _step_ == 201: break

    _lamp_coord[0] =  7
    _lamp_coord[1] = -7
    _photos = 'photo' + str(_step_)
    _main_catalogist = os.path.join(_dir, _photos)
    bpy.data.scenes["Scene"].render.filepath = _main_catalogist
    bpy.ops.render.render(write_still=True)
    _step_degrees += 0.0125
    _step_ += 1
    if _step_ == 201: break

    _lamp_coord[0] =  6.5
    _lamp_coord[1] = -7.5
    _photos = 'photo' + str(_step_)
    _main_catalogist = os.path.join(_dir, _photos)
    bpy.data.scenes["Scene"].render.filepath = _main_catalogist
    bpy.ops.render.render(write_still=True)
    _step_degrees += 0.0125
    _step_ += 1
    if _step_ == 201: break

    _lamp_coord[0] =  6
    _lamp_coord[1] = -8
    _photos = 'photo' + str(_step_)
    _main_catalogist = os.path.join(_dir, _photos)
    bpy.data.scenes["Scene"].render.filepath = _main_catalogist
    bpy.ops.render.render(write_still=True)
    _step_degrees += 0.0125
    _step_ += 1
    if _step_ == 201: break
