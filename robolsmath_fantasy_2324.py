from manim import *
from math import *

config.disable_caching = False
main_bg = [DARK_GRAY,BLACK]

class fantasy(Scene):
    def construct(self):
      gradient_colors = main_bg
      bg = Rectangle(width = config.frame_width,height = config.frame_height, stroke_width = 0,
                       fill_color = gradient_colors,fill_opacity = 1)
      self.add(bg)
      
      # values and score
      vals = {'Aaron' : [0,7,13,18,21,26,30,37,41.5,47.5,48.5,53.5,56.5,58,65,69,74,80,87,92,99],'Gian' : [0,3,8,12,16.5,21.5,26.5,33.5,34.5,38.5,43.5,46.5,51.5,59.5,61.5,64.5,69.5,76.5,80.5,82.5,88.5],'Jake' : [0,2,6,12,17,18,20,22,26,31,35,39,42,43,48,54,56,59,61,64,66],'JD' : [0,7,10,16,22,28.5,34.5,39.5,47.5,54.5,60.5,65.5,71.5,79,87,95,103,107,110,117,122.5],'Jeffrey' : [0,6,10,13,20.5,28.5,33.5,40.5,46.5,50.5,56.5,60.5,64.5,66.5,70.5,75.5,82.5,85.5,92.5,100.5,104],'Masa' : [0,2,4,7,11,15,18,20,26,32,35,40,46,53,57,62,65.5,70.5,75.5,82.5,87.5],'MJ' : [0,4,8,15,16.5,21.5,28.5,32.5,37,42,48,52,57,59,67,71,76.5,82.5,88.5,92.5,95.5],'Niel' : [0,4,9,11,16,18.5,22.5,25.5,27.5,32.5,37.5,41.5,43.5,48.5,49.5,53.5,54.5,56.5,58.5,65.5,71],'Ryan' : [0,8,13,19,23,27,32,40,47,50,53,59,60,67,72,75,79,83,89,91,95],'Sethe' : [0,1,6,9,15,21,26,32,35,37,41,46,54,61,65,70,73,78.5,85.5,87.5,91],'Shawn' : [0,5,9,15,18,22,26,27,30,34,42,46,50,54,59,60,64,67.5,70.5,71.5,78.5],'Toffee' : [0,5,12,15,19.5,22.5,26.5,28.5,33.5,36.5,39.5,44.5,51.5,53.5,54.5,60.5,66.5,71.5,73.5,79.5,81.5]}
      matchups = [ [ ['Ryan vs Sethe', '8-1'],['Aaron vs Masa', '7-2'],['Jeffrey vs Gian', '6-3'],['Shawn vs MJ', '5-4'],['Niel vs Toffee', '4-5'],['Jake vs JD', '2-7'] ],[ ['Toffee vs Masa', '7-2'],['Ryan vs MJ', '5-4'],['Niel vs Shawn', '5-4'],['Jeffrey vs Sethe', '4-5'],['Jake vs Gian', '4-5'],['JD vs Aaron', '3-6'] ],[ ['JD vs Toffee', '6-3'],['Shawn vs Masa', '6-3'],['Jake vs Sethe', '6-3'],['Gian vs Aaron', '4-5'],['Jeffrey vs Ryan', '3-6'],['Niel vs MJ', '2-7'] ],[ ['Jeffrey vs MJ', '7-1-1'],['JD vs Shawn', '6-3'],['Niel vs Masa', '5-4'],['Ryan vs Jake', '4-5'],['Gian vs Toffee', '4-4-1'],['Aaron vs Sethe', '3-6'] ],[ ['Jeffrey vs Jake', '8-1'],['JD vs Niel', '6-2-1'],['MJ vs Masa', '5-4'],['Ryan vs Aaron', '4-5'],['Shawn vs Gian', '4-5'],['Toffee vs Sethe', '3-6'] ],[ ['JD vs Masa', '6-3'],['Jeffrey vs Aaron', '5-4'],['Ryan vs Toffee', '5-4'],['Niel vs Gian', '4-5'],['Shawn vs Sethe', '4-5'],['Jake vs MJ', '2-7'] ],[ ['Ryan vs Shawn', '8-1'],['Jeffrey vs Toffee', '7-2'],['Gian vs Masa', '7-2'],['JD vs MJ', '5-4'],['Niel vs Sethe', '3-6'],['Jake vs Aaron', '2-7'] ],[ ['JD vs Gian', '8-1'],['Ryan vs Niel', '7-2'],['Jeffrey vs Shawn', '6-3'],['Masa vs Sethe', '6-3'],['Jake vs Toffee', '4-5'],['MJ vs Aaron', '4-4-1'] ],[ ['JD vs Sethe', '7-2'],['Jake vs Shawn', '5-4'],['Jeffrey vs Niel', '4-5'],['Gian vs MJ', '4-5'],['Ryan vs Masa', '3-6'],['Toffee vs Aaron', '3-6'] ],[ ['Shawn vs Aaron', '8-1'],['Jeffrey vs Masa', '6-3'],['MJ vs Toffee', '6-3'],['Gian vs Sethe', '5-4'],['Jake vs Niel', '4-5'],['Ryan vs JD', '3-6'] ],[ ['Ryan vs Gian', '6-3'],['Jeffrey vs JD', '4-5'],['Jake vs Masa', '4-5'],['Niel vs Aaron', '4-5'],['Shawn vs Toffee', '4-5'],['MJ vs Sethe', '4-5'] ],[ ['Jeffrey vs Gian', '4-5'],['Shawn vs MJ', '4-5'],['Jake vs JD', '3-6'],['Aaron vs Masa', '3-6'],['Niel vs Toffee', '2-7'],['Ryan vs Sethe', '1-8'] ],[ ['Niel vs Shawn', '5-4'],['Jeffrey vs Sethe', '2-7'],['Toffee vs Masa', '2-7'],['Jake vs Gian', '1-8'],['JD vs Toffee', '8-1'],['Jake vs Sethe', '5-4'] ],[ ['Shawn vs Masa', '5-4'],['Jeffrey vs Ryan', '4-5'],['Gian vs Aaron', '2-7'],['Niel vs MJ', '1-8'],['JD vs Shawn', '8-1'],['Jeffrey vs MJ', '5-4'] ],[ ['Niel vs Masa', '4-5'],['Aaron vs Sethe', '4-5'],['Ryan vs Jake', '3-6'],['Gian vs Toffee', '3-6'],['JD vs Niel', '8-1'],['Jeffrey vs Jake', '7-2'] ],[ ['JD vs Niel', '8-1'],['Jeffrey vs Jake', '7-2'],['Toffee vs Sethe', '6-3'],['MJ vs Masa', '5-3-1'],['Ryan vs Aaron', '4-5'],['Shawn vs Gian', '4-5'] ],[ ['Ryan vs Toffee', '4-5'],['JD vs Masa', '4-5'],['Jeffrey vs Aaron', '3-6'],['Jake vs MJ', '3-6'],['Shawn vs Sethe', '3-5-1'],['Niel vs Gian', '2-7'] ],[ ['Jeffrey vs Toffee', '7-2'],['Ryan vs Shawn', '6-3'],['Gian vs Masa', '4-5'],['JD vs MJ', '3-6'],['Jake vs Aaron', '2-7'],['Niel vs Sethe', '2-7'] ],[ ['Jeffrey vs Shawn', '8-1'],['JD vs Gian', '7-2'],['Masa vs Sethe', '7-2'],['MJ vs Aaron', '4-5'],['Jake vs Toffee', '3-6'],['Ryan vs Niel', '2-7'] ],[ ['Gian vs MJ', '6-3'],['JD vs Sethe', '5-3-1'],['Ryan vs Masa', '4-5'],['Jeffrey vs Niel', '3-5-1'],['Jake vs Shawn', '2-7'],['Toffee vs Aaron', '2-7'] ] ]

      # Initialize ranks with empty lists for each player
      ranks = {player: [] for player in vals}

      # Number of rounds is the length of the score list of any player
      num_rounds = len(next(iter(vals.values())))

      # Loop through each round
      for round_idx in range(num_rounds):
          # Create a list of tuples (player, score) for the current round
          round_scores = [(player, scores[round_idx]) for player, scores in vals.items()]

          # Sort by score; if there's a tie, use previous rank as a tiebreaker
          if round_idx == 0:
              # For the first round, sort by score and then alphabetically by player name to break ties
              sorted_scores = sorted(round_scores, key=lambda x: (x[1], x[0]), reverse=True)
          else:
              # For subsequent rounds, use the previous round's rank as a tiebreaker
              sorted_scores = sorted(
                  round_scores,
                  key=lambda x: (x[1], -ranks[x[0]][-1]),  # Sort by score (descending) and previous rank (ascending)
                  reverse=True
              )

          # Assign ranks and update ranks
          for rank, (player, _) in enumerate(sorted_scores, start=1):
              ranks[player].append(rank)

      ##################################################
      max_height = 4.5
      max_width = 10

      N = len(vals) # number of items
      bar_height = max_height/N*0.9
      bar_width_ratio = max_width/max([d[-1] for d in list(vals.values())])
      print(bar_width_ratio)

      list_colors = color_gradient([BLUE, GREEN, RED],N)
      print(list_colors)
      vg_dots = VGroup(*[Dot(0.01) for _ in range(N)]).arrange(DOWN, buff = max_height/N).to_edge(LEFT,buff = 2.5)

      vg_text = VGroup()
      vg_bars = VGroup()
      vg_scores = VGroup()

      list_keys = list(vals.keys())

      for i in range(N):
        p = list_keys[i]

        vg_text.add(Text(p,color = list_colors[i], font = "Courier New", font_size = 20).next_to(vg_dots[i],LEFT,buff =0.1))

        vg_bars.add(Rectangle(height = bar_height, width = 0, fill_color = list_colors[i], fill_opacity = 1, stroke_width = 0.00001).next_to(vg_dots[i],RIGHT,buff =0.1))
        vg_scores.add(Text("0",color = list_colors[i], font = "Courier New", font_size = 20).next_to(vg_bars[i],LEFT,buff =0.1))


      vg_matchups = VGroup()
      vg_week = VGroup()
      for i in range(len(matchups)):
        vg_matchups.add(Table(
            matchups[i],
            col_labels=[Text("Matchup"), Text("Result")],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": TEAL}
        ).scale_to_fit_height(2).next_to(vg_text[-1],RIGHT,aligned_edge = DOWN).to_edge(RIGHT,buff = 1)
        )

        vg_matchups[-1].add(vg_matchups[-1].get_cell((1, 1),color = TEAL, fill_opacity=0.25, stroke_width = 1))
        vg_matchups[-1].add(vg_matchups[-1].get_cell((1, 2),color = TEAL,fill_opacity=0.25, stroke_width = 1))

        vg_week.add(Text("WEEK " + str(i+1), color = TEAL, font_size = 20).next_to(vg_matchups[-1],UP,buff = 0.1))


      self.wait(1)
      self.play(*(FadeIn(txt, run_time = 1.5, rate_func = linear) for txt in vg_text),)
      self.wait(2)

      for round in range(1,len(vals[list_keys[0]])):
        vg_bars_new = VGroup(
            *[Rectangle(height = bar_height, width = vals[list_keys[i]][round]*bar_width_ratio, fill_color = list_colors[i], fill_opacity = 1, stroke_width = 0.00001).next_to(vg_dots[ranks[list_keys[i]][round]-1],RIGHT,buff =0.1) for i in range(N)]
        )
        vg_scores_new = VGroup(*[Text(str(vals[list_keys[i]][round]),color = list_colors[i], font = "Courier New", font_size = 20).next_to(vg_bars_new[i],RIGHT,buff = 0.1) for i in range(N)])

        if round > 1:
          tbl_anim = [ReplacementTransform(vg_matchups[round-2],vg_matchups[round-1]),
                    ReplacementTransform(vg_week[round-2],vg_week[round-1])]
        else:
          tbl_anim = [FadeIn(vg_matchups[round-1]),FadeIn(vg_week[round-1])]

        self.play(*[ReplacementTransform(vg_bars[i],vg_bars_new[i]) for i in range(N)],
                  *[vg_text[i].animate.next_to(vg_dots[ranks[list_keys[i]][round]-1],LEFT,buff =0.1) for i in range(N)],
                  *[ReplacementTransform(vg_scores[i],vg_scores_new[i]) for i in range(N)],
                  *tbl_anim,
                  run_time = 2)

        vg_bars = vg_bars_new
        vg_scores = vg_scores_new
        self.wait(0.5)

      self.wait(5)