class SceneBuilder:
    def __init__(self):
        self.scene_registry = {}

    def register_scene(self, scene_code, scene_creator):
        # Пов'язує код сцени з створюваннням сцени
        self.scene_registry[scene_code] = scene_creator

    def create_scene(self, scene_code, screen, manager, *args):
        # Якщо сцена зареєстрована, повертає екземпляр сцени
        if scene_code not in self.scene_registry:
            return
        return self.scene_registry[scene_code](screen, manager, *args)
