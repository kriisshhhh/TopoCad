# Create your views here.
from django.shortcuts import render

# Importing topologic library
import topologic
import topologicpy
from topologicpy.Cell import Cell
from topologicpy.CellComplex import CellComplex
from topologicpy.Face import Face
from topologicpy.Vertex import Vertex
from topologicpy.Topology import Topology

def say_hello(request):
    return render(request, 'hello.html')


def generate_cube(request):
    # Create a CellComplex for Cube
    Og = Vertex.ByCoordinates(0,0,0)
    x = 10
    y = 10
    z = 10
    u = 2
    v = 2
    w = 2
    cube_og = CellComplex.Prism(origin=Og, uSides=u, vSides=v, wSides=w, width=y, length=x, height=z)
    cube = Topology.Triangulate(cube_og)
    cube_data = Topology.Geometry(cube)

    cube_vertices = cube_data['vertices']
    cube_edges = cube_data['edges']
    cube_faces = cube_data['faces']

    # Create a CellComplex for Torus
    r1 = 5.0
    r2 = 1.5
    tu = 12
    tv = 8
    torus_og = Cell.Torus(origin=Og, majorRadius=r1, minorRadius=r2, uSides=tu, vSides=tv, direction=[0,1,0])
    torus = Topology.Triangulate(torus_og)
    torus_data = Topology.Geometry(torus)

    torus_vertices = torus_data['vertices']
    torus_edges = torus_data['edges']
    torus_faces = torus_data['faces']

    # Create a CellComplex for Cylinder
    rc1 = 3
    hc = 8
    uc = 11
    vc = 1
    cylinder_og = Cell.Cylinder(origin=Og, radius=rc1, height=hc, uSides=uc, vSides=vc, direction=[0,1,0])
    cylinder = Topology.Triangulate(cylinder_og)
    cylinder_data = Topology.Geometry(cylinder)

    cylinder_vertices = cylinder_data['vertices']
    cylinder_edges = cylinder_data['edges']
    cylinder_faces = cylinder_data['faces']

    # Create a CellComplex for Sphere
    rs = 3
    us = 16
    vs = 8
    sphere_og = Cell.Sphere(origin=Og, radius=rs, uSides=us, vSides=vs, direction=[0,1,0])
    sphere = Topology.Triangulate(sphere_og)
    sphere_data = Topology.Geometry(sphere)

    sphere_vertices = sphere_data['vertices']
    sphere_edges = sphere_data['edges']
    sphere_faces = sphere_data['faces']

    cube_context = {
        'cube_vertices': cube_vertices,
        'cube_edges': cube_edges,
        'cube_faces': cube_faces,

        'torus_vertices': torus_vertices,
        'torus_edges': torus_edges,
        'torus_faces': torus_faces,

        'cylinder_vertices': cylinder_vertices,
        'cylinder_edges': cylinder_edges,
        'cylinder_faces': cylinder_faces,

        'sphere_vertices': sphere_vertices,
        'sphere_edges': sphere_edges,
        'sphere_faces': sphere_faces
    }

    # Render the HTML template with the cube_data
    return render(request, 'editor/cube.html', cube_context)

