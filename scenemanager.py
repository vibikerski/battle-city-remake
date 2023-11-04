class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None
        self.next_scene = None
    
    def add_scene(self, scene_code, scene):
        self.scenes[scene_code] = scene 
    
    def set_scene(self, scene_code):
        if not self.current_scene:
            self.current_scene = scene_code
        elif scene_code in self.scenes:
            self.next_scene = scene_code
        
    def run(self, events):
        active_scene = self.scenes[self.current_scene]
        active_scene.handle_events(events)
        active_scene.update()
        active_scene.render()
        
        if self.next_scene:
            self.current_scene = self.next_scene
            self.next_scene = None