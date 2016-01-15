from vispy.color import BaseColormap

def get_translucent_cmap(r, g, b):
    
    class TranslucentCmap(BaseColormap):
        glsl_map = """
        vec4 translucent_fire(float t) {{
            return vec4(t * {0}, t * {1}, t * {2}, max(0, t*1.05 - 0.05));
        }}
        """.format(r, g, b)
        
    return TranslucentCmap()