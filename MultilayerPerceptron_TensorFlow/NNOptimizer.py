# -*- coding:utf-8 -*-
# Anaconda 4.3.0 環境 (TensorFlow インストール済み)

"""
    更新情報
    [17/11/18] : 新規作成
    [17/xx/xx] : 
               : 
"""

import numpy

# TensorFlow ライブラリ
import tensorflow as tf
from tensorflow.python.framework import ops


class NNOptimzer( object ):
    """
    ニューラルネットワークの最適化アルゴリズム Optimizer を表すクラス
    実際の最適化アルゴリズムを表すクラスの実装は、このクラスを継承し、オーバーライドするを想定している。
    ------------------------------------------------------------------------------------------------
    [public] public アクセス可能なインスタスンス変数には, 便宜上変数名の最後にアンダースコア _ を付ける.
        _optimizer : Optimizer
            最適化アルゴリズム
        _train_step : 
            トレーニングステップ
        _node_name : str
            この Optimizer ノードの名前

        _learning_rate : float
            学習率 (0.0~1.0)
            
    [protedted] protedted な使用法を想定 
        
    [private] 変数名の前にダブルアンダースコア __ を付ける（Pythonルール）

    """
    def __init__( self, learning_rate = 0.001, node_name = "Optimizer" ):
        self._optimizer = None
        self._train_step = None
        self._node_name = node_name
        self._learning_rate = learning_rate

        return

    def print( str ):
        print( "NNOptimizer" )
        print( self )
        print( str )
        print( "_optimizer :", self._optimizer )
        print( "_train_step :", self._train_step )
        print( "_node_name :", self._node_name )
        print( "_learning_rate :", self._learning_rate )

        return

    def optimizer( self ):
        """
        最適化アルゴリズム Optimizer の設定を行う。

        [Output]
            optimizer
        """
        return self._optimizer


    def train_step( self, loss_op ):
        """
        トレーニングステップの設定を行う。

        [Input]
            loss_op : Operation
                損失関数のオペレーター

        [Output]
            optimizer のトレーニングステップ
        """
        return self._train_step


class GradientDecent( NNOptimzer ):
    """
    最急降下法を表すクラス
    NNOptimizer クラスの子クラスとして定義
    """
    def __init__( self, learning_rate = 0.001, node_name = "GradientDecent_Optimizer" ):
        self._learning_rate = learning_rate
        self._node_name = node_name
        self._optimizer = self.optimizer()
        self._train_step = None

        return
    
    def optimizer( self ):
        self._optimizer = tf.train.GradientDescentOptimizer( learning_rate = self._learning_rate )
        return self._optimizer

    def train_step( self, loss_op ):
        self._train_step = self._optimizer.minimize( loss_op )
        return self._train_step


class Momentum( NNOptimzer ):
    """
    モメンタム アルゴリズムを表すクラス
    NNOptimizer クラスの子クラスとして定義
    """
    def __init__( self, learning_rate = 0.001, momentum = 0.9, node_name = "Momentum_Optimizer" ):
        self._learning_rate = learning_rate
        self._momentum = momentum
        self._node_name = node_name
        self._optimizer = self.optimizer()
        self._train_step = None

        return
    
    def optimizer( self ):
        self._optimizer = tf.train.MomentumOptimizer( 
                              learning_rate = self._learning_rate, 
                              momentum = self._momentum,
                              use_nesterov = False
                          )

        return self._optimizer

    def train_step( self, loss_op ):
        self._train_step = self._optimizer.minimize( loss_op )
        return self._train_step


class NesterovMomentum( NNOptimzer ):
    """
    Nesterov モメンタム アルゴリズムを表すクラス
    NNOptimizer クラスの子クラスとして定義
    """
    def __init__( self, learning_rate = 0.001, momentum = 0.9, node_name = "NesterovMomentum_Optimizer" ):
        self._learning_rate = learning_rate
        self._momentum = momentum
        self._node_name = node_name
        self._optimizer = self.optimizer()
        self._train_step = None

        return
    
    def optimizer( self ):
        self._optimizer = tf.train.MomentumOptimizer( 
                              learning_rate = self._learning_rate, 
                              momentum = self._momentum,
                              use_nesterov = True
                          )

        return self._optimizer

    def train_step( self, loss_op ):
        self._train_step = self._optimizer.minimize( loss_op )
        return self._train_step


class Adagrad( NNOptimzer ):
    """
    Adagrad アルゴリズムを表すクラス
    NNOptimizer クラスの子クラスとして定義
    """
    def __init__( self, learning_rate = 0.001, node_name = "Adagrad_Optimizer" ):
        self._learning_rate = learning_rate
        self._node_name = node_name
        self._optimizer = self.optimizer()
        self._train_step = None

        return
    
    def optimizer( self ):
        self._optimizer = tf.train.AdagradOptimizer( learning_rate = self._learning_rate )
        return self._optimizer

    def train_step( self, loss_op ):
        self._train_step = self._optimizer.minimize( loss_op )
        return self._train_step


class Adadelta( NNOptimzer ):
    """
    Adadelta アルゴリズムを表すクラス
    NNOptimizer クラスの子クラスとして定義
    """
    def __init__( self, learning_rate = 0.001, rho = 0.95, node_name = "Adadelta_Optimizer" ):
        self._learning_rate = learning_rate
        self._rho = rho
        self._node_name = node_name
        self._optimizer = self.optimizer()
        self._train_step = None

        return
    
    def optimizer( self ):
        self._optimizer = tf.train.AdadeltaOptimizer( learning_rate = self._learning_rate, rho = self._rho )
        return self._optimizer

    def train_step( self, loss_op ):
        self._train_step = self._optimizer.minimize( loss_op )
        return self._train_step

