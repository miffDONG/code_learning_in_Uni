using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class Item
{
    public string name; // �̸�
    public int health; // ü��
    public int damage; // ���ݷ�
    public int hitType;
    // BlueGun : �⺻(0), GreenGun : ������ 2��(1), YellowGun : ����(2), RedGun: ��(���ӵ�)(3), Slow: �ӵ� ������(4), Bomb: ��ź(5), Wall: ���к�(6)
    public int maxDistance; // ���� ����
    // �� �̿� �ø� ���, Bomb, Wall ����
    public float regenTime; // �Ѿ� ���� �ð�
    public float gunSpeed; // �Ѿ� �ӵ�
    public GameObject AstroPre; // Prefab
    public GameObject bulletPre; // bullet prefab
}

[CreateAssetMenu(fileName = "ItemSO", menuName = "Scriptable Object/ItemSO")]
public class ItemSO : ScriptableObject
{
    public Item[] items;
}
