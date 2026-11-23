from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random
from ball import Ball

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)
    game_world.add_collision_pair('grass:ball', grass, None)

    global balls

    balls = [Ball(random.randint(0, 1700), 60, 0) for i in range(30)]
    game_world.add_objects(balls, 1)

    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)

    game_world.add_collision_pair("boy:ball", boy, None) #boy가 중복되니까 이런식으로 작성
    for ball in balls:
        #game_world.add_collision_pair("boy:ball", boy, ball) #이렇게하면 boy가 중복됨
        game_world.add_collision_pair("boy:ball", None, ball) #boy가 중복되니까 이렇게 작성

    for zombie in zombies:
        game_world.add_collision_pair("zombie:ball", zombie, ball)
        

def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    #global boy
    #game_world.update()
    # 소년과 볼이 만나는지 충돌 확인이 필요하다. 모든 볼에 대해서

    # for ball in balls[:]: #balls라는 리스트를 하나 복사해서 만들어서 새로운 balls가 생김
    #     if game_world.collid(boy, ball):
    #         print("COLLISION boy <-> ball") #일단 프린트 충돌 결과
    #         boy.ball_count += 1
    #         game_world.remove_object(ball)
    #         balls.remove(ball)

    game_world.update()
    game_world.handle_collisions()




def render():
    clear_canvas()
    game_world.render()
    update_canvas()









