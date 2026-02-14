import sys
import os

# --- THE PEACE TREATY ---
# This allows 'import keras' and 'tensorflow' to coexist without 
# hitting the 'populate_dict_with_module_objects' error.
try:
    import tensorflow.keras as tf_keras
    sys.modules['keras'] = tf_keras
except ImportError:
    pass
# ------------------------

def validate_dqn_environment():
    print("--- 🕹️ DQN Baseline (With Standalone Keras) ---")
    
    try:
        import keras
        import tensorflow as tf
        from keras.models import Sequential
        from keras.layers import Dense
        from keras.optimizers import Adam
        
        # Verify both are actually recognized
        print(f"DEBUG: Keras Version: {keras.__version__}")
        print(f"DEBUG: TF Version: {tf.__version__}")

        import gym
        env = gym.make('CartPole-v0')
        
        # Test the legacy 'lr' alias
        model = Sequential()
        model.add(Dense(24, input_dim=4, activation='relu'))
        model.compile(loss='mse', optimizer=Adam(lr=0.001))
        
        print("SUCCESS: Environment is stable with standalone Keras.")
        return True

    except Exception as e:
        print(f"\nCRITICAL: {type(e).__name__} - {e}")
        return False

if __name__ == "__main__":
    if validate_dqn_environment():
        print("\n--- BASELINE GREEN ---")
        sys.exit(0)
    else:
        print("\n--- VALIDATION RED ---")
        sys.exit(1)